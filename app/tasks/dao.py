from sqlalchemy import insert

from app.dao.base import BaseDAO
from app.database import async_session_maker
from app.tasks.models import Tasks


class TasksDAO(BaseDAO):
    model = Tasks

    @classmethod
    async def add(cls, task_name):
        pass
        # async with async_session_maker() as session:
        #     query = insert(cls.model).values(data)
        #     await session.execute(query)
        #     await session.commit()
