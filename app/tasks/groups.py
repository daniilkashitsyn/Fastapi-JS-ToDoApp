from fastapi import APIRouter

router = APIRouter(prefix="/groups", tags=["Groups page"])


@router.get("/")
def get_groups():
    return "This is group page"
