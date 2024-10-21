from app.database import Base
from sqlalchemy import Column, Integer, String, Date, JSON, ForeignKey


class Users(Base):
    __tablename__ = "Users"

    id = Column(Integer, primary_key=True, autoincrement=True)
    nickname = Column(String, nullable=False)
    email = Column(String, nullable=False)
    hashed_password = Column(String, nullable=False)
    completed_tasks = Column(Integer, nullable=False, default=0)
    progress_tasks = Column(Integer, nullable=False, default=0)
    archived_tasks = Column(Integer, nullable=False, default=0)