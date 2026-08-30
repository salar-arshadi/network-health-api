from fastapi import APIRouter

from app.services.collector_service import CollectorService
from app.schemas.collector import LinuxCollectorResponse
from app.schemas.device import LinuxCollectorRequest

router = APIRouter(
    prefix="/collect",
    tags=["Collector"],
)


@router.post(
    "/linux",
    summary="Collect Linux Metrics",
    description="Connects to a Linux server over SSH and returns system metrics.",
    response_model=LinuxCollectorResponse,
)
def collect_linux(request: LinuxCollectorRequest):

    return CollectorService.collect_linux(request)
