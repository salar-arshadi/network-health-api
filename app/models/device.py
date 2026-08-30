from sqlalchemy import Column, Integer, String, DateTime
from datetime import datetime

from app.database import Base


class Device(Base):
    __tablename__ = "devices"

    id = Column(Integer, primary_key=True, index=True)

    hostname = Column(String(100), nullable=False)
    ip_address = Column(String(50), nullable=False, unique=True)
    management_ip = Column(String(50), nullable=True)

    device_type = Column(String(30), nullable=False)
    vendor = Column(String(50), nullable=False)
    model = Column(String(100), nullable=True)
    serial_number = Column(String(100), nullable=True)

    operating_system = Column(String(100), nullable=True)

    location = Column(String(100), nullable=True)
    rack = Column(String(50), nullable=True)

    status = Column(String(30), default="active")

    created_at = Column(DateTime, default=datetime.utcnow)
