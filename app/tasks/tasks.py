from fastapi import APIRouter

from app.tasks.dao import TasksDAO


router = APIRouter(prefix="/tasks", tags=["Задачи"])


@router.get("")
async def get_tasks():
    return await TasksDAO.find_all()


@router.get("/{task_id}")
async def get_task(task_id):

