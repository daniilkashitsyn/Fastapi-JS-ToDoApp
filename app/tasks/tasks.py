from fastapi import APIRouter


router = APIRouter(prefix="/tasks", tags=["Tasks page"])

@router.get("/")
def get_tasks():
    return "This is Tasks page"