from fastapi import APIRouter, Depends

from app.exceptions import GroupNotFoundException
from app.tasks.dao import GroupsDAO
from app.tasks.shemas import SGroups
from app.users.dependencies import get_current_user
from app.users.users import Users


router = APIRouter(prefix="/groups", tags=["Группы задач"])


@router.get("/")
async def get_groups(user: Users = Depends(get_current_user)) -> list[SGroups]:
    return await GroupsDAO.find_all(user_id=user.id)


@router.get("/{group_id}")
async def get_group(group_id: int, user: Users = Depends(get_current_user)) -> SGroups:
    group = await GroupsDAO.find_by_id_and_user(id=group_id, user_id=user.id)
    if not group:
        raise GroupNotFoundException
    return group
