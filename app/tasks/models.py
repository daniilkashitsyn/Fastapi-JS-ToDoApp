from app.database import Base
from sqlalchemy import Column, Integer, String, Date, ForeignKey


class Tasks(Base):
    __tablename__ = "tasks"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    description = Column(String, nullable=False)
    group_id = Column(ForeignKey("groups.id"))
    start_date = Column(Date)
    end_date = Column(Date)
    priority = Column(String)
    status = Column(String)
    user_id = Column(ForeignKey("Users.id"), nullable=False)


class Groups(Base):
    __tablename__ = "groups"

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    tasks_id = Column(ForeignKey("tasks.id"))
    user_id = Column(ForeignKey("Users.id"), nullable=False)
