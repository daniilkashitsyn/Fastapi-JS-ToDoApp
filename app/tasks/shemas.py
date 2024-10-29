from datetime import date

from pydantic import BaseModel


class STasks(BaseModel):
    id: int
    name: str
    description: str
    group_id: int
    start_date: date
    end_date: date
    priority: str
    status: str

    class Config:
        from_attributes = True


class SGroups(BaseModel):
    id: int
    name: str

    class Config:
        from_attributes = True
