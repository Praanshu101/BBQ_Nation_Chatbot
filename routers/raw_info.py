from fastapi import APIRouter, Query, HTTPException
from fastapi import APIRouter, Query, HTTPException
from utils.dataloader import load_data
import logging

logging.basicConfig(level=logging.DEBUG)
router = APIRouter()

@router.get("/")
def get_raw_info(query: str = Query(..., min_length=3)):
    try:
        logging.debug(f"Received query: {query}")
        data = load_data()
        # Filter raw information based on the query
        raw_info = [item for item in data if query.lower() in item["branch.name"].lower()]
        if not raw_info:
            return {"message": "No raw information found for the given query."}
        return {"answer": raw_info}
    except Exception as e:
        logging.error(f"Error in /raw endpoint: {e}")
        raise HTTPException(status_code=500, detail="An unexpected error occurred.")

from services.response_formatter import format_nearest_outlets

@router.get("/nearest")
def nearest_outlets(city: str = Query(...)):
    try:
        logging.debug(f"Received city: {city}")
        data = load_data()
        nearest_outlets = format_nearest_outlets(data, city)
        if not nearest_outlets:
            return {"nearest_outlets": "No outlets found in the specified city."}
        return {"nearest_outlets": nearest_outlets}
    except Exception as e:
        logging.error(f"Error in /raw/nearest endpoint: {e}")
        raise HTTPException(status_code=500, detail="An unexpected error occurred.")