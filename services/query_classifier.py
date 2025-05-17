def classify_query(query: str) -> str:
    query = query.lower()
    if any(word in query for word in ["timing", "open", "close", "hours"]):
        return "timing"
    if any(word in query for word in ["offer", "discount", "deal"]):
        return "offers"
    if any(word in query for word in ["address", "location", "nearby"]):
        return "location"
    if any(word in query for word in ["menu", "food", "starter", "veg", "non-veg", "dish"]):
        return "menu"
    return "general"