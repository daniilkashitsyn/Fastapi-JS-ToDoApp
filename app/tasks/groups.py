from fastapi import APIRouter

router = APIRouter(prefix="/groups", tags=["Группы задач"])


@router.get("/")
def get_groups():
    return "pages"
