from pydantic import BaseModel, Field


class LinuxCollectorRequest(BaseModel):
    host: str = Field(..., example="192.168.1.100")
    username: str = Field(..., example="monitor")
    password: str = Field(..., example="secret")
    port: int = Field(22, example=22)
