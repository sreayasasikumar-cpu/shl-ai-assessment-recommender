import json
from sentence_transformers import SentenceTransformer

# Load catalog
with open("catalog.json", "r", encoding="utf-8") as f:
    catalog = json.load(f)

# Load embedding model
model = SentenceTransformer("all-MiniLM-L6-v2")

# Prepare text for embeddings
texts = [
    item["name"] + " " + item["description"] + " " + item["test_type"]
    for item in catalog
]

# Generate embeddings
embeddings = model.encode(texts)

print("Embeddings created successfully!")
print(f"Total assessments: {len(embeddings)}")