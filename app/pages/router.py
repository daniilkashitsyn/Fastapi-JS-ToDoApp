from fastapi import APIRouter, Request, Depends
from fastapi.templating import Jinja2Templates

from app.tasks.dao import TasksDAO
from app.tasks.tasks import get_tasks, get_task
from app.tasks.groups import get_groups, get_group
from app.users.router import get_current_user

router = APIRouter(
    prefix="/pages",
    tags=["Фронтэнд"]
)

templates = Jinja2Templates(directory="app/templates")


@router.get("/tasks")
async def get_tasks_page(request: Request, tasks=Depends(get_tasks)):
    return templates.TemplateResponse(
        name="tasks.html",
        context={"request": request, "tasks": tasks}
    )


@router.get("/tasks/{task_id}")
async def get_task_by_id(request: Request, task_id: int, user=Depends(get_current_user)):
    task = await get_task(task_id=task_id, user=user)
    return templates.TemplateResponse(
        name="task.html",
        context={"request": request, "task": task}
    )


@router.get("/groups/{group_id}")
async def get_group_by_id(request: Request, group_id: int, user=Depends(get_current_user)):
    group = await get_group(group_id=group_id, user=user)
    tasks = await TasksDAO.get_tasks_by_group(group_id=group_id)
    return templates.TemplateResponse(
        name="group.html",
        context={"request": request, "group": group, "tasks": tasks}
    )


@router.get("/login")
async def login_page(request: Request):
    return templates.TemplateResponse(
        name="auth/login.html",
        context={"request": request}
    )


@router.get("/reg")
async def reg_page(request: Request):
    return templates.TemplateResponse(
        name="auth/registration.html",
        context={"request": request}
    )


@router.get("/main")
async def main_page(request: Request):
    return templates.TemplateResponse(
        name="main.html",
        context={"request": request}
    )


@router.get("/groups")
async def groups_page(request: Request, groups=Depends(get_groups)):
    return templates.TemplateResponse(
        name="groups.html",
        context={"request": request, "groups": groups}
    )


@router.get("/create-task")
async def add_task_page(request: Request):
    return templates.TemplateResponse(
        name="addtask.html",
        context={"request": request}
    )
