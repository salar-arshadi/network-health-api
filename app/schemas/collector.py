from pydantic import BaseModel, ConfigDict

class CpuInfo(BaseModel):
    usage_percent: float
    idle_percent: float


class MemoryInfo(BaseModel):
    total_gb: float
    used_gb: float
    free_gb: float
    available_gb: float
    cache_gb: float

    model_config = ConfigDict(
        json_schema_extra={
            "example": {
                "total_gb": 32,
                "used_gb": 8,
                "free_gb": 18,
                "available_gb": 24,
                "cache_gb": 6,
            }
        }
    )


class DiskInfo(BaseModel):
    filesystem: str
    size_gb: float
    used_gb: float
    available_gb: float
    usage_percent: int
    mount: str

    model_config = ConfigDict(
        json_schema_extra={
            "example": {
                "filesystem": "/dev/sda1",
                "size_gb": 512,
                "used_gb": 181,
                "available_gb": 331,
                "usage_percent": 35,
                "mount": "/",
            }
        }
    )


class LinuxCollectorResponse(BaseModel):
    hostname: str
    uptime: str
    cpu: CpuInfo
    memory: MemoryInfo
    disk: DiskInfo

    model_config = ConfigDict(
        json_schema_extra={
            "example": {
                "hostname": "server01",
                "uptime": "5 days, 12:44",
                "cpu": "%Cpu(s): 2.3 us, 1.1 sy, 96.6 id",
                "memory": {
                    "total_gb": 32,
                    "used_gb": 8,
                    "free_gb": 18,
                    "available_gb": 24,
                    "cache_gb": 6,
                },
                "disk": {
                    "filesystem": "/dev/sda1",
                    "size_gb": 512,
                    "used_gb": 181,
                    "available_gb": 331,
                    "usage_percent": 35,
                    "mount": "/",
                },
            }
        }
    )
