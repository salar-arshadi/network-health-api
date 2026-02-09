from fastapi import FastAPI
import psutil
import socket
import asyncio

from app.core.logging import setup_logging, get_logger
from app.core.scheduler import collect_metrics
from app.api.metrics import router as metrics_router
from app.api.health import router as health_router  # 👈 NEW

# ----------------------
# logging setup
# ----------------------
setup_logging()
logger = get_logger("api")

# ----------------------
# FastAPI app
# ----------------------
app = FastAPI(title="Network & System Health API")

# ----------------------
# scheduler task holder
# ----------------------
scheduler_task: asyncio.Task | None = None


# ----------------------
# lifecycle events
# ----------------------
@app.on_event("startup")
async def on_startup():
    global scheduler_task

    logger.info("API startup completed")

    # start background scheduler
    scheduler_task = asyncio.create_task(
        collect_metrics(interval=10)
    )

    logger.info("Metrics scheduler started")


@app.on_event("shutdown")
async def on_shutdown():
    logger.warning("API shutting down")

    if scheduler_task:
        scheduler_task.cancel()
        try:
            await scheduler_task
        except asyncio.CancelledError:
            logger.info("Metrics scheduler stopped cleanly")


# ----------------------
# endpoints (simple system info)
# ----------------------
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


# ----------------------
# routers
# ----------------------
app.include_router(metrics_router)
app.include_router(health_router)  # 👈 NEW

