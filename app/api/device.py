from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database import get_db
from app.models import Device

from app.schemas.device_create import DeviceCreate
from app.schemas.device_response import DeviceResponse

router = APIRouter(
    prefix="/devices",
    tags=["Devices"],
)


@router.post(
    "/",
    response_model=DeviceResponse,
    summary="Create Device",
)
def create_device(
    request: DeviceCreate,
    db: Session = Depends(get_db),
):

    device = Device(
        hostname=request.hostname,
        ip_address=request.ip_address,
        management_ip=request.management_ip,
        device_type=request.device_type,
        vendor=request.vendor,
        model=request.model,
        serial_number=request.serial_number,
        operating_system=request.operating_system,
        location=request.location,
        rack=request.rack,
        status=request.status,
    )

    db.add(device)
    db.commit()
    db.refresh(device)

    return device


@router.get(
    "/",
    response_model=list[DeviceResponse],
    summary="List Devices",
)
def get_devices(
    db: Session = Depends(get_db),
):

    return db.query(Device).all()


@router.get(
    "/{device_id}",
    response_model=DeviceResponse,
)
def get_device(
    device_id: int,
    db: Session = Depends(get_db),
):

    device = (
        db.query(Device)
        .filter(Device.id == device_id)
        .first()
    )

    if not device:
        raise HTTPException(
            status_code=404,
            detail="Device not found",
        )

    return device


@router.delete("/{device_id}")
def delete_device(
    device_id: int,
    db: Session = Depends(get_db),
):

    device = (
        db.query(Device)
        .filter(Device.id == device_id)
        .first()
    )

    if not device:
        raise HTTPException(
            status_code=404,
            detail="Device not found",
        )

    db.delete(device)
    db.commit()

    return {
        "message": "Device deleted"
    }
