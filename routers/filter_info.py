from fastapi import APIRouter, Query, HTTPException
from services.response_formatter import format_response
from utils.dataloader import load_data
from services.tokenizer_utils import trim_to_token_limit
import logging

logging.basicConfig(level=logging.DEBUG)
router = APIRouter()

@router.get("/")
def filter_information(query: str = Query(..., min_length=3)):
    try:
        logging.debug(f"Received query: {query}")
        data = load_data()
        response = format_response(data, query)
        if not response:
            return {"message": "No relevant information found."}
        # Trim response to 800 tokens if necessary
        response = trim_to_token_limit(response, max_tokens=800)
        return {"answer": response}
    except Exception as e:
        logging.error(f"Error in /info endpoint: {e}")
        raise HTTPException(status_code=500, detail="An unexpected error occurred.")