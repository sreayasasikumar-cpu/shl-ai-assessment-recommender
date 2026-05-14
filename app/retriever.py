import json
import numpy as np
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

# Load catalog
with open("catalog.json", "r", encoding="utf-8") as f:
    catalog = json.load(f)

# Load embedding model
model = SentenceTransformer("all-MiniLM-L6-v2")

# Prepare text data
texts = [
    item["name"] + " " + item["description"] + " " + item["test_type"]
    for item in catalog
]

# Generate embeddings
embeddings = model.encode(texts)

def retrieve_assessments(query, top_k=3):
    # Encode query
    query_embedding = model.encode([query])

    # Compute similarity
    similarities = cosine_similarity(query_embedding, embeddings)[0]

    # Get ranked indices
    top_indices = np.argsort(similarities)[::-1]

    results = []

    for idx in top_indices:
        item = catalog[idx]

        # Simple refinement rules
        if "personality" in query.lower():
            if item["test_type"].lower() != "personality":
                continue

        if "technical" in query.lower():
            if item["test_type"].lower() != "technical":
                continue

        results.append({
            "name": item["name"],
            "url": item["url"],
            "description": item["description"],
            "test_type": item["test_type"],
            "score": float(similarities[idx])
        })

        if len(results) >= top_k:
            break

    return results