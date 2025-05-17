from fastapi import APIRouter

router = APIRouter()

@router.get("/")
def health_check():
    return {"status": "ok"}

@router.get("/version")
def version():
    return {"version": "1.0"}
