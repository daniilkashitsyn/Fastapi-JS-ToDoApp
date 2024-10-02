from app.database import Base
from sqlalchemy import Column, Integer, String, Date, JSON


class Tasks(Base):
    __tablename__ = "tasks"

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    description = Column(String, nullable=False)
    # group = Column(String)
    start_date = Column(Date)
    end_date = Column(Date)
    priority = Column(JSON, nullable=False)
    status = Column(JSON, nullable=False)


class Groups(Base):
    __tablename__ = "groups"

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    # tasks = Column(String)
