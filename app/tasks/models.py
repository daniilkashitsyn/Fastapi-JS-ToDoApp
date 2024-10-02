from app.database import Base
from sqlalchemy import Column, Integer, String, Date


class Tasks(Base):
    __tablename__ = "tasks"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    description = Column(String)
    start_date = Column(Date)
    end_date = Column(Date)
    priority = Column()
    status = Column()


class Groups(Base):
    pass
