from fastapi import FastAPI
from app.api.research import router as research_router

app = FastAPI(title="ResearchOS API")

app.include_router(
    research_router,
    prefix="/research",
    tags=["Research"]
)