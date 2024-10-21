from app.dao.base import BaseDAO
from app.database import async_session_maker
from sqlalchemy import delete

from app.users.users import Users


class UsersDAO(BaseDAO):
    model = Users

    
