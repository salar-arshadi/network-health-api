import asyncio
import psutil
from datetime import datetime
from sqlalchemy.orm import Session

from app.database import SessionLocal
from app.models import SystemMetric
from app.core.logging import get_logger

logger = get_logger("scheduler")


async def collect_metrics(interval: int = 10):
    logger.info("🟢 Metrics scheduler started")

    try:
        while True:
            logger.info("⏱ Collecting system metrics")

            db: Session = SessionLocal()
            try:
                metric = SystemMetric(
                    cpu=psutil.cpu_percent(interval=1),
                    memory=psutil.virtual_memory().percent,
                    disk=psutil.disk_usage("/").percent,
                )
                db.add(metric)
                db.commit()

                logger.info("✅ Metrics saved")

            except Exception as e:
                logger.exception("❌ Scheduler error")

            finally:
                db.close()

            await asyncio.sleep(interval)

    except asyncio.CancelledError:
        logger.warning("🟡 Metrics scheduler stopped")
        raise

