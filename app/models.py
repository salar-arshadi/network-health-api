from sqlalchemy import Column, Integer, Float, DateTime
from datetime import datetime
from .database import Base

class SystemMetric(Base):
    __tablename__ = "system_metrics"

    id = Column(Integer, primary_key=True, index=True)
    cpu = Column(Float, nullable=False)
    memory = Column(Float, nullable=False)
    disk = Column(Float, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)
