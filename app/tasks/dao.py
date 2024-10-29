from app.dao.base import BaseDAO
from app.tasks.models import Tasks, Groups


class TasksDAO(BaseDAO):
    model = Tasks

    @classmethod
    async def change_group(cls, group_name):
        pass


class GroupsDAO(BaseDAO):
    model = Groups

