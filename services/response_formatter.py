from typing import List, Dict
import logging

# Logging configuration
logging.basicConfig(level=logging.DEBUG)


def trim_to_token_limit(response: str, max_tokens: int = 800) -> str:
    tokens = response.split()
    if len(tokens) > max_tokens:
        return " ".join(tokens[:max_tokens]) + "..."
    return response

def format_response(data: List[Dict], query: str) -> str:
    # Dummy: Filter outlets with query keywords, combine info, trimmed to 800 tokens handled elsewhere
    results = []
    query_lower = query.lower()
    for outlet in data:
        if query_lower in str(outlet).lower():
            results.append(outlet.get("branch.name", "Unknown branch"))
    return ", ".join(results) if results else ""

def format_raw_info(data: List[Dict], query: str) -> str:
    # Return detailed JSON string for matching outlet
    query_lower = query.lower()
    for outlet in data:
        if query_lower in str(outlet).lower():
            import json
            # Trim to token limit
            outlet_str = json.dumps(outlet, indent=2)
            if len(outlet_str) > 800:
                outlet_str = trim_to_token_limit(outlet_str)
            outlet = json.loads(outlet_str)
            return json.dumps(outlet, indent=2)
    return ""

def get_nearest_outlets(data, city: str):
    try:
        outlets = [outlet for outlet in data if outlet["city"].lower() == city.lower()]
        if not outlets:
            return []
        return sorted(outlets, key=lambda x: x["distance_km"])
    except KeyError as e:
        logging.error(f"Missing key in data: {e}")
        return []


def format_nearest_outlets(data: List[Dict], city: str) -> List[str]:
    nearest_outlets = [outlet for outlet in data if outlet.get("city", "").lower() == city.lower()]
    if not nearest_outlets:
        return []
    
    formatted_outlets = []
    for outlet in nearest_outlets:
        formatted_outlets.append(f"{outlet['branch.name']} - {outlet['address']}, {outlet['pincode']}")
    
    return formatted_outlets

def format_feedback_response(feedback: str) -> str:
    # Dummy: Just return the feedback text
    return f"Feedback received: {feedback}"

def format_classification_response(classification: str) -> str:
    # Dummy: Just return the classification text
    return f"Query classified as: {classification}"

def format_health_check_response() -> str:
    # Dummy: Just return a health check message
    return "Service is running and healthy."