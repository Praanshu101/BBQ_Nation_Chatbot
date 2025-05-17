import logging
from pathlib import Path

LOG_FILE = Path("logs/app.log")  # updated relative path
LOG_FILE.parent.mkdir(parents=True, exist_ok=True)

logging.basicConfig(filename=LOG_FILE, level=logging.INFO, format='%(asctime)s %(message)s')

def log_feedback(feedback_text: str):
    logging.info(f"FEEDBACK: {feedback_text}")

def log_unhandled_query(query_text: str):
    logging.info(f"UNHANDLED QUERY: {query_text}")

def log_unusual_query(query_text: str):
    logging.warning(f"UNUSUAL QUERY: {query_text}")