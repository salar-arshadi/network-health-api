from fastapi import FastAPI
import psutil
import socket

from app.api.metrics import router as metrics_router

app = FastAPI(title="Network & System Health API")


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


# 👇 register routers
app.include_router(metrics_router)
