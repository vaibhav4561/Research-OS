from sqlalchemy import Column, Integer, String, Text, DateTime
from sqlalchemy.sql import func

from app.database.database import Base


class ResearchReport(Base):
    __tablename__ = "research_reports"

    id = Column(Integer, primary_key=True, index=True)

    topic = Column(String(255), nullable=False)

    search_results = Column(Text, nullable=False)

    scraped_content = Column(Text, nullable=False)

    report = Column(Text, nullable=False)

    feedback = Column(Text, nullable=False)

    created_at = Column(
        DateTime(timezone=True),
        server_default=func.now()
    )