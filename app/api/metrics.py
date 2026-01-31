from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
import psutil

from app.database import get_db
from app.models import SystemMetric

router = APIRouter(
    prefix="/metrics",
    tags=["Metrics"],
)


@router.post("/")
def save_metrics(db: Session = Depends(get_db)):
    metric = SystemMetric(
        cpu=psutil.cpu_percent(interval=1),
        memory=psutil.virtual_memory().percent,
        disk=psutil.disk_usage("/").percent,
    )

    db.add(metric)
    db.commit()
    db.refresh(metric)

    return {
        "status": "saved",
        "id": metric.id,
    }


@router.get("/latest")
def latest_metric(db: Session = Depends(get_db)):
    metric = (
        db.query(SystemMetric)
        .order_by(SystemMetric.created_at.desc())
        .first()
    )

    if not metric:
        return {"message": "no data"}

    return {
        "cpu": metric.cpu,
        "memory": metric.memory,
        "disk": metric.disk,
        "created_at": metric.created_at,
    }

