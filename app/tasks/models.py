from app.database import Base
from sqlalchemy import Column, Integer, String, Date, JSON


class Tasks(Base):
    __tablename__ = "tasks"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    description = Column(String)
    # group = Column(String)
    start_date = Column(Date)
    end_date = Column(Date)
    priority = Column(JSON)
    status = Column(JSON)


class Groups(Base):
    __tablename__ = "groups"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    # tasks = Column(String)
