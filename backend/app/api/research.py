from fastapi import APIRouter
from app.models.research import ResearchRequest
from app.services.pipeline import run_research_pipeline


router = APIRouter()


@router.get("/")
def test():
    return {"status": "Research API Working"}


@router.post("/")
def research(request: ResearchRequest):

    report = run_research_pipeline(request.query)

    return report