from datetime import date

from pydantic import BaseModel
from typing import Optional


class STasks(BaseModel):
    id: int
    name: str
    description: Optional[str] = None
    group_id: Optional[int] = None
    start_date: Optional[date] = None
    end_date: Optional[date] = None
    priority: Optional[str] = None
    status: Optional[str] = None

    class Config:
        from_attributes = True


class STaskCreate(BaseModel):
    name: str
    description: Optional[str] = None
    start_date: Optional[date] = None
    end_date: Optional[date] = None
    priority: Optional[str] = None
    status: Optional[str] = None

    class Config:
        from_attributes = True


class STaskChange(BaseModel):
    name: Optional[str] = None
    description: Optional[str] = None
    start_date: Optional[date] = None
    end_date: Optional[date] = None
    priority: Optional[str] = None
    status: Optional[str] = None

    class Config:
        from_attributes = True


class SGroups(BaseModel):
    id: int
    name: str

    class Config:
        from_attributes = True


class SGroupCreate(BaseModel):
    name: str

    class Config:
        from_attributes = True
