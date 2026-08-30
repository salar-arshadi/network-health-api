from pydantic import BaseModel


class DeviceUpdate(BaseModel):
    hostname: str | None = None
    ip_address: str | None = None
    management_ip: str | None = None

    device_type: str | None = None
    vendor: str | None = None

    model: str | None = None
    serial_number: str | None = None
    operating_system: str | None = None

    location: str | None = None
    rack: str | None = None

    status: str | None = None
