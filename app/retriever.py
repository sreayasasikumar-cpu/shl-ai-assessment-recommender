import json

# Load catalog
with open("app/catalog.json", "r", encoding="utf-8") as f:
    catalog = json.load(f)

def retrieve_assessments(query, top_k=3):
    query = query.lower()

    scored_results = []

    for item in catalog:
        score = 0

        text = (
            item["name"] + " " +
            item["description"] + " " +
            item["test_type"]
        ).lower()

        # Simple keyword matching
        for word in query.split():
            if word in text:
                score += 1

        # Filter personality queries
        if "personality" in query:
            if item["test_type"].lower() != "personality":
                continue

        # Filter technical queries
        if "technical" in query:
            if item["test_type"].lower() != "technical":
                continue

        scored_results.append((score, item))

    # Sort by score
    scored_results.sort(reverse=True, key=lambda x: x[0])

    results = []

    for score, item in scored_results[:top_k]:
        results.append({
            "name": item["name"],
            "url": item["url"],
            "description": item["description"],
            "test_type": item["test_type"],
            "score": score
        })

    return results