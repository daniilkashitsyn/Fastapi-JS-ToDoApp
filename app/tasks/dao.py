from sqlalchemy import insert, update, select

from app.dao.base import BaseDAO
from app.database import async_session_maker
from app.tasks.models import Tasks, Groups


class TasksDAO(BaseDAO):
    model = Tasks

    @classmethod
    async def create_task(cls, name: str, description: str, start_date, end_date, priority: str,
                          status: str, user_id: int):
        async with async_session_maker() as session:
            query = insert(cls.model).values(
                name=name,
                description=description,
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

    @classmethod
    async def get_tasks_by_group(cls, group_id: int):
        async with async_session_maker() as session:
            query = select(cls.model).filter_by(group_id=group_id)
            result = await session.execute(query)
            return result.scalars().all()


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
