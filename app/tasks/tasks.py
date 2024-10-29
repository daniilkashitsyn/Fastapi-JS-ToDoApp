from fastapi import APIRouter, Depends

from app.exceptions import TaskNotFoundException
from app.tasks.dao import TasksDAO
from app.tasks.shemas import STasks
from app.users.dependencies import get_current_user
from app.users.users import Users

router = APIRouter(prefix="/tasks", tags=["Задачи"])


@router.get("/")
async def get_tasks(user: Users = Depends(get_current_user)) -> list[STasks]:
    return await TasksDAO.find_all(user_id=user.id)


@router.get("/{task_id}")
async def get_task(task_id: int, user: Users = Depends(get_current_user)) -> STasks:
    task = await TasksDAO.find_by_id_and_user(task_id, user.id)
    if not task:
        raise TaskNotFoundException
    return task
