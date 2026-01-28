from fastapi import FastAPI
import psutil
import socket

from sqlalchemy.orm import Session
from app.database import engine, SessionLocal
from app.models import Base, SystemMetric

app = FastAPI(title="Network & System Health API")


@app.on_event("startup")
def on_startup():
    Base.metadata.create_all(bind=engine)


@app.get("/health")
def health_check():
    return {"status": "ok"}


@app.get("/system")
def system_status():
    return {
        "cpu_percent": psutil.cpu_percent(interval=1),
        "memory_percent": psutil.virtual_memory().percent,
        "disk_percent": psutil.disk_usage("/").percent,
    }


@app.get("/network")
def network_status():
    hostname = socket.gethostname()
    ip_address = socket.gethostbyname(hostname)
    return {
        "hostname": hostname,
        "ip_address": ip_address,
    }


@app.post("/metrics")
def save_metrics():
    db: Session = SessionLocal()
    try:
        metric = SystemMetric(
            cpu=psutil.cpu_percent(interval=1),
            memory=psutil.virtual_memory().percent,
            disk=psutil.disk_usage("/").percent,
        )

        db.add(metric)
        db.commit()
        db.refresh(metric)

        return {"status": "saved", "id": metric.id}
    finally:
        db.close()


@app.get("/metrics/latest")
def latest_metric():
    db: Session = SessionLocal()
    try:
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
    finally:
        db.close()
