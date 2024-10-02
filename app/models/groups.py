from pydantic import BaseModel


class Group(BaseModel):
    group_id: int
    group_name: str
    # group_tasks:
