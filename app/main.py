from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

import asyncio
import psutil
import socket

from app.database import Base, engine

from app.core.logging import (
    setup_logging,
    get_logger,
)

from app.core.scheduler import collect_metrics

# Import all models
from app import models

# Routers
from app.api.auth import router as auth_router
from app.api.collector import router as collector_router
from app.api.device import router as device_router
from app.api.health import router as health_router
from app.api.metrics import router as metrics_router


# ============================================================
# Logging
# ============================================================

setup_logging()

logger = get_logger("api")


# ============================================================
# OpenAPI Tags
# ============================================================

tags_metadata = [

    {
        "name": "Authentication",
        "description": "Authentication endpoints.",
    },

    {
        "name": "Infrastructure",
        "description": "Information about the DataCenter Monitor host.",
    },

    {
        "name": "Collector",
        "description": "Collect metrics from monitored infrastructure.",
    },

    {
        "name": "Devices",
        "description": "Manage monitored devices.",
    },

    {
        "name": "Metrics",
        "description": "Collected infrastructure metrics.",
    },

    {
        "name": "Health",
        "description": "Liveness and readiness endpoints.",
    },

]


# ============================================================
# FastAPI
# ============================================================

app = FastAPI(

    title="Zitel Data Center Operations Platform AAPI",

    description="""
REST API for Zitel Data Center Operations Platform.

Provides authentication,
inventory management,
monitoring,
metrics,
automation,
and future DCIM capabilities.
""",

    version="1.0.0",

    contact={
        "name": "Zitel",
        "email": "support@zitel.local",
    },

    servers=[
        {
            "url": "http://localhost:8000",
            "description": "Local Development",
        }
    ],

    openapi_tags=tags_metadata,

)


# ============================================================
# CORS
# ============================================================

app.add_middleware(

    CORSMiddleware,

    allow_origins=[
        "http://localhost:5173",
        "http://localhost:5174",
    ],

    allow_credentials=True,

    allow_methods=["*"],

    allow_headers=["*"],

)


# ============================================================
# Scheduler
# ============================================================

scheduler_task: asyncio.Task | None = None


# ============================================================
# Startup
# ============================================================

@app.on_event("startup")
async def startup():

    global scheduler_task

    logger.info("API starting...")

    Base.metadata.create_all(bind=engine)

    scheduler_task = asyncio.create_task(
        collect_metrics(interval=10)
    )

    logger.info("Scheduler started")


# ============================================================
# Shutdown
# ============================================================

@app.on_event("shutdown")
async def shutdown():

    logger.info("API shutting down")

    if scheduler_task:

        scheduler_task.cancel()

        try:

            await scheduler_task

        except asyncio.CancelledError:

            logger.info("Scheduler stopped")


# ============================================================
# Infrastructure
# ============================================================

@app.get("/system", tags=["Infrastructure"])
def system_status():

    return {

        "cpu": psutil.cpu_percent(),

        "memory": psutil.virtual_memory().percent,

        "disk": psutil.disk_usage("/").percent,

    }


@app.get("/network", tags=["Infrastructure"])
def network_status():

    hostname = socket.gethostname()

    ip = socket.gethostbyname(hostname)

    return {

        "hostname": hostname,

        "ip_address": ip,

    }


# ============================================================
# Routers
# ============================================================

app.include_router(auth_router)

app.include_router(collector_router)

app.include_router(device_router)

app.include_router(metrics_router)

app.include_router(health_router)
