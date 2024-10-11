from app.database import Base
from sqlalchemy import Column, Integer, String, Date, JSON, ForeignKey


class Tasks(Base):
    __tablename__ = "tasks"

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    description = Column(String, nullable=False)
    group_id = Column(ForeignKey("groups.id"))
    start_date = Column(Date)
    end_date = Column(Date)
    priority = Column(JSON)
    status = Column(JSON)


class Groups(Base):
    __tablename__ = "groups"

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    tasks_id = Column(ForeignKey("tasks.id"))
