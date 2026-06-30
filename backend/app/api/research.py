from fastapi import APIRouter
from app.models.research import ResearchRequest
from app.services.pipeline import run_research_pipeline
from fastapi import Depends
from sqlalchemy.orm import Session
import json
from app.database.database import get_db
from app.database.models import ResearchReport
from fastapi import HTTPException


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

@router.get("/history")
def get_history(db: Session = Depends(get_db)):
    reports = (
        db.query(ResearchReport)
        .order_by(ResearchReport.created_at.desc())
        .all()
    )

    return reports

@router.get("/history/{report_id}")
def get_report(report_id: int, db: Session = Depends(get_db)):
    report = (
        db.query(ResearchReport)
        .filter(ResearchReport.id == report_id)
        .first()
    )

    if report is None:
        raise HTTPException(
            status_code=404,
            detail="Research report not found"
        )

    return report