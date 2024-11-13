from fastapi import APIRouter, Depends

from app.database import async_session_maker
from app.exceptions import TaskNotFoundException, GroupNotFoundException
from app.tasks.dao import TasksDAO, GroupsDAO
from app.tasks.shemas import STasks, STaskCreate, STaskChange
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


@router.post("/add-task")
async def add_task(task_data: STaskCreate, user: Users = Depends(get_current_user)):
    if task_data.group_id:
        group = await GroupsDAO.find_by_id_and_user(id=task_data.group_id, user_id=user.id)
        if group is None:
            raise GroupNotFoundException
    await TasksDAO.create_task(
        name=task_data.name,
        description=task_data.description,
        group_id=task_data.group_id,
        start_date=task_data.start_date,
        end_date=task_data.end_date,
        priority=task_data.priority,
        status=task_data.status,
        user_id=user.id
    )
    return {"message": "Задача создана"}


@router.patch("{task_id}/ch")
async def change_task_by_id(task_id: int, task_data: STaskChange, user: Users = Depends(get_current_user)):
    task = await GroupsDAO.find_by_id_and_user(id=task_id, user_id=user.id)
    if task is None:
        raise TaskNotFoundException
    update_data = task_data.dict(exclude_unset=True)
    if update_data:
        await TasksDAO.change_task(task_id=task_id, data=update_data)
    return {"message": "Задача успешно обновлена"}


@router.delete("{task_id}/del")
async def delete_task_by_id(task_id: int, user: Users = Depends(get_current_user)):
    task = await TasksDAO.find_by_id_and_user(id=task_id, user_id=user.id)
    if task is None:
        raise TaskNotFoundException
    await TasksDAO.delete_by_id_and_user(id=task_id, user_id=user.id)
    return {"message": "Задача удалена"}
