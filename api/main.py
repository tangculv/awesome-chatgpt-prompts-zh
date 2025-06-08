from fastapi import FastAPI
from pydantic import BaseModel
from typing import List, Optional

app = FastAPI()

class Device(BaseModel):
    id: int
    name: str
    category: str
    is_active: bool

# 模拟的设备数据库
DEVICES_DB = [
    Device(id=1, name="Router A", category="router", is_active=True),
    Device(id=2, name="Switch B", category="switch", is_active=False),
    Device(id=3, name="Camera C", category="camera", is_active=True),
]

class DeviceFilter(BaseModel):
    category: Optional[str] = None

@app.post("/api/v2/devices/active", response_model=List[Device])
def get_active_devices(filter: DeviceFilter):
    """返回 is_active 為 True 的設備列表，可選擇按 category 過濾"""
    if filter.category:
        return [d for d in DEVICES_DB if d.is_active and d.category == filter.category]
    return [d for d in DEVICES_DB if d.is_active]
