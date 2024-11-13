from fastapi import APIRouter, Depends

from app.exceptions import GroupNotFoundException
from app.tasks.dao import GroupsDAO
from app.tasks.shemas import SGroups, SGroupCreate
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


@router.post("/add-group")
async def add_group(group_data: SGroupCreate, user: Users = Depends(get_current_user)):
    await GroupsDAO.create_group(
        name=group_data.name,
        user_id=user.id
    )

    return {"message": "Группа создана"}


@router.patch("{group_id}/change")
async def change_group(group_id: int, group_data: SGroupCreate, user: Users = Depends(get_current_user)):
    group = await GroupsDAO.find_by_id_and_user(id=group_id, user_id=user.id)
    if group is None:
        raise GroupNotFoundException
    update_data = group_data.dict(exclude_unset=True)
    await GroupsDAO.change_group(group_id=group_id, data=update_data)
    return {"message": "Группа обновлена"}


@router.delete("{group_id}/delete")
async def delete_group(group_id: int, user: Users = Depends(get_current_user)):
    group = await GroupsDAO.find_by_id_and_user(id=group_id, user_id=user.id)
    if group is None:
        raise GroupNotFoundException
    await GroupsDAO.delete_by_id_and_user(id=group_id, user_id=user.id)
    return {"message": "Группа удалена"}
