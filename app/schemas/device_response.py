from datetime import datetime

from pydantic import BaseModel, ConfigDict


class DeviceResponse(BaseModel):
    id: int

    hostname: str
    ip_address: str
    management_ip: str | None

    device_type: str
    vendor: str

    model: str | None
    serial_number: str | None
    operating_system: str | None

    location: str | None
    rack: str | None

    status: str | None

    created_at: datetime | None

    model_config = ConfigDict(
        from_attributes=True
    )
