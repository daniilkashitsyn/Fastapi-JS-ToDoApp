from fastapi import APIRouter

from app.tasks.dao import TasksDAO
from app.tasks.shemas import STasks


router = APIRouter(prefix="/tasks", tags=["Задачи"])


@router.get("/")
async def get_tasks() -> list[STasks]:
    return await TasksDAO.find_all()


@router.get("/{task_id}")
async def get_task(task_id: int) -> STasks:
    return await TasksDAO.find_by_id(task_id)
