import json

# Load catalog
with open("app/catalog.json", "r", encoding="utf-8") as f:
    catalog = json.load(f)

def retrieve_assessments(query, top_k=3):
    query_lower = query.lower()

    scored_results = []

    for item in catalog:
        score = 0

        text = (
            item["name"] + " " +
            item["description"] + " " +
            item["test_type"]
        ).lower()

        # Keyword scoring
        for word in query_lower.split():
            if word in text:
                score += 1

        test_type = item["test_type"].lower()

        # Technical filtering
        if (
            "technical" in query_lower or
            "developer" in query_lower or
            "programming" in query_lower or
            "coding" in query_lower or
            "python" in query_lower or
            "java" in query_lower or
            "sql" in query_lower
        ):
            if test_type != "technical":
                continue

        # Personality filtering
        if "personality" in query_lower:
            if test_type != "personality":
                continue

        # Leadership filtering
        if (
            "leadership" in query_lower or
            "manager" in query_lower or
            "management" in query_lower
        ):
            if test_type != "leadership":
                continue

        # Communication filtering
        if (
            "customer service" in query_lower or
            "communication" in query_lower or
            "support" in query_lower or
            "call center" in query_lower
        ):
            if test_type != "communication":
                continue

        # Cognitive filtering
        if (
            "cognitive" in query_lower or
            "reasoning" in query_lower or
            "aptitude" in query_lower or
            "numerical" in query_lower or
            "deductive" in query_lower or
            "inductive" in query_lower
        ):
            if test_type != "cognitive":
                continue

        scored_results.append((score, item))

    # Sort by score descending
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