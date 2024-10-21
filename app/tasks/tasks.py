from fastapi import APIRouter, Request, Depends

from app.tasks.dao import TasksDAO
from app.tasks.shemas import STasks
from app.users.dependencies import get_current_user
from app.users.users import Users

router = APIRouter(prefix="/tasks", tags=["Задачи"])


@router.get("/")
async def get_tasks(user: Users = Depends(get_current_user)) -> list[STasks]:
    return await TasksDAO.find_all(user_id=user.id)


@router.get("/task")
async def get_task():  # -> list[STasks]:
    pass
