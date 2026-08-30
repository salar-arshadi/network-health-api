from pydantic import BaseModel, Field


class DeviceCreate(BaseModel):
    hostname: str = Field(..., examples=["linux-01"])
    ip_address: str = Field(..., examples=["192.168.1.10"])

    management_ip: str | None = None

    device_type: str = Field(..., examples=["linux"])
    vendor: str = Field(..., examples=["Ubuntu"])

    model: str | None = None
    serial_number: str | None = None
    operating_system: str | None = None

    location: str | None = None
    rack: str | None = None

    status: str = "Healthy"
