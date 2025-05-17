# main.py
from fastapi import FastAPI
from routers import filter_info, classify, health, feedback, raw_info

app = FastAPI(title="Barbeque Nation Info API")

app.include_router(health.router, prefix="/health")
app.include_router(filter_info.router, prefix="/info")
app.include_router(classify.router, prefix="/classify")
app.include_router(feedback.router, prefix="/feedback")
app.include_router(raw_info.router, prefix="/raw")

@app.get("/")
def root():
    return {"message": "Welcome to the BBQ Nation Info API"}

from fastapi import HTTPException, Request
from fastapi.responses import JSONResponse

@app.exception_handler(HTTPException)
async def http_exception_handler(request: Request, exc: HTTPException):
    return JSONResponse(status_code=exc.status_code, content={"error": exc.detail})

@app.exception_handler(Exception)
async def general_exception_handler(request: Request, exc: Exception):
    return JSONResponse(status_code=500, content={"error": "An unexpected error occurred."})
