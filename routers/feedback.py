from fastapi import APIRouter, Request

from utils.cache import log_feedback

router = APIRouter()

@router.post("/")
async def log_user_feedback(request: Request):
    data = await request.json()
    feedback_text = data.get("feedback")
    if not feedback_text:
        return {"status": "error", "message": "Feedback text missing"}
    log_feedback(feedback_text)
    return {"status": "success", "message": "Feedback logged"}
