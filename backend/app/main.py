from fastapi import FastAPI
from app.api.research import router as research_router
from app.database.database import engine
from sqlalchemy import text
from app.database.models import ResearchReport
from app.database.database import Base

app = FastAPI(title="ResearchOS API")

@app.on_event("startup")
def test_database():
    try:
        Base.metadata.create_all(bind=engine)

        with engine.connect() as connection:
            connection.execute(text("SELECT 1"))

        print("✅ Database connected successfully!")
        print("✅ Tables created successfully!")

    except Exception as e:
        print("❌ Database connection failed!")
        print(e)

app.include_router(
    research_router,
    prefix="/research",
    tags=["Research"]
)