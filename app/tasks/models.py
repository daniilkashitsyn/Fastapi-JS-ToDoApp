from app.database import Base
from sqlalchemy import Column, Integer, String, Date, JSON, ForeignKey, Enum
from sqlalchemy.orm import relationship


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
    user_id = Column(ForeignKey("Users.id"))
    user = relationship("User", back_populates="tasks")


class Groups(Base):
    __tablename__ = "groups"

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    tasks_id = Column(ForeignKey("tasks.id"))
    user_id = Column(ForeignKey("Users.id"))
    user = relationship("User", back_populates="groups")
