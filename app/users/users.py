from app.database import Base
from sqlalchemy import Column, Integer, String, Date, JSON, ForeignKey

class Users(Base):
    __tablename__ = "Users"

    id = Column(Integer, primary_key=True)
    nickname = Column(String, nullable=False)
    email = Column(String, nullable=False)
    hashed_password = Column(String, nullable=False)
    completed_tasks = Column(Integer, nullable=False)
    progress_tasks = Column(Integer, nullable=False)
    archived_tasks = Column(Integer, nullable=False)