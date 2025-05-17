from fastapi import APIRouter, Query
from services.query_classifier import classify_query
from utils.dataloader import load_veg_starters
import logging
from fastapi import HTTPException

logging.basicConfig(level=logging.DEBUG)
router = APIRouter()

@router.get("/")
def classify(query: str = Query(..., min_length=3)):
    try:
        logging.debug(f"Received query: {query}")
        classification = classify_query(query)
        if classification == "menu":
            veg_starters = load_veg_starters()
            starters_list = ", ".join(veg_starters)
            return {
                "classification": classification,
                "response": f"The veg starters available are {starters_list}."
            }
        return {"classification": classification, "response": "Query not recognized."}
    except Exception as e:
        logging.error(f"Error in /classify endpoint: {e}")
        raise HTTPException(status_code=500, detail="An unexpected error occurred.")