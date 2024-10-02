from datetime import date
from pydantic import BaseModel


class Task(BaseModel):
    task_id: int
    task_name: str
    task_description: str
    date_start: date
    date_end: date
   # task_status:
