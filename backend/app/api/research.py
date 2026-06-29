from fastapi import APIRouter
from app.models.research import ResearchRequest
from app.services.pipeline import run_research_pipeline
from fastapi import Depends
from sqlalchemy.orm import Session
import json
from app.database.database import get_db
from app.database.models import ResearchReport


router = APIRouter()


@router.get("/")
def test():
    return {"status": "Research API Working"}


@router.post("/")
def research(
    request: ResearchRequest,
    db: Session = Depends(get_db)
):
    report = run_research_pipeline(request.query)

    new_report = ResearchReport(
        topic=request.query,
        search_results=json.dumps(report["search_results"]),
        scraped_content=report["scraped_content"],
        report=report["report"],
        feedback=report["feedback"],
    )

    db.add(new_report)
    db.commit()
    db.refresh(new_report)

    return report