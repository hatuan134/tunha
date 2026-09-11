from fastapi import FastAPI
from sqlalchemy import text
from sqlalchemy.exc import SQLAlchemyError

from app.core.config import get_settings
from app.core.database import engine

settings = get_settings()
app = FastAPI(title=settings.app_name)


@app.get("/health", tags=["health"])
def health() -> dict[str, object]:
    database = "ok"
    try:
        with engine.connect() as connection:
            connection.execute(text("SELECT 1"))
    except SQLAlchemyError:
        database = "unavailable"

    return {
        "status": "ok" if database == "ok" else "degraded",
        "core": "ok",
        "database": database,
        "ai_provider": "optional",
    }


@app.get(f"{settings.api_v1_prefix}/status", tags=["system"])
def api_status() -> dict[str, str]:
    return {"service": settings.app_name, "status": "available"}
