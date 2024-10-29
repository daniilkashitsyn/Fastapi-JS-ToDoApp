from fastapi import APIRouter, Request, Depends
from fastapi.templating import Jinja2Templates

from app.tasks.tasks import get_tasks

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
