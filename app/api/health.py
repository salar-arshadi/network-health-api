from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from sqlalchemy import text

from app.database import get_db

router = APIRouter(
    prefix="/health",
    tags=["Health"],
)

@router.get("/live")
def liveness_check():
    """
    Liveness probe
    - Simply checks whether the application process is running.
    - No external dependencies are verified here.
    """
    return {"status": "alive"}

@router.get("/ready")
def readiness_check(db: Session = Depends(get_db)):
    """
    Readiness probe
    - Verifies that the application is ready to receive traffic.
    - Checks database connectivity.
    """
    try:
        db.execute(text("SELECT 1"))
        return {"status": "ready"}
    except Exception:
        return {"status": "not ready"}

