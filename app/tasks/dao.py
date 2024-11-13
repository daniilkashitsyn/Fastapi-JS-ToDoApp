from sqlalchemy import insert, update

from app.dao.base import BaseDAO
from app.database import async_session_maker
from app.tasks.models import Tasks, Groups


class TasksDAO(BaseDAO):
    model = Tasks

    @classmethod
    async def create_task(cls, name: str, description: str, group_id: int, start_date, end_date, priority: str,
                          status: str, user_id: int):
        async with async_session_maker() as session:
            query = insert(cls.model).values(
                name=name,
                description=description,
                group_id=group_id,
                start_date=start_date,
                end_date=end_date,
                priority=priority,
                status=status,
                user_id=user_id
            )

            await session.execute(query)
            await session.commit()

    @classmethod
    async def change_task(cls, task_id: int, data):
        async with async_session_maker() as session:
            query = update(cls.model).where(cls.model.id == task_id).values(**data)
            await session.execute(query)
            await session.commit()


class GroupsDAO(BaseDAO):
    model = Groups

    @classmethod
    async def create_group(cls, name: str, user_id: int):
        async with async_session_maker() as session:
            query = insert(cls.model).values(
                name=name,
                user_id=user_id
            )

            await session.execute(query)
            await session.commit()

    @classmethod
    async def change_group(cls, group_id: int, data):
        async with async_session_maker() as session:
            query = update(cls.model).where(cls.model.id == group_id).values(data)
            await session.execute(query)
            await session.commit()
