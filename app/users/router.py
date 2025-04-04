from fastapi import APIRouter, Response, Depends

from app.exceptions import UserAlreadyExistsException, IncorrectEmailOrPasswordException
from app.users.auth import get_password_hash, authenticate_user, create_access_token
from app.users.dao import UsersDAO
from app.users.dependencies import get_current_user, get_current_admin_user
from app.users.schemas import SUserAuth, SUserReg
from app.users.users import Users

router = APIRouter(
    prefix="/auth",
    tags=["Auth & Пользователи"]
)


@router.post("/register")
async def register_user(user_data: SUserReg):
    existing_user = await UsersDAO.find_one_or_none(email=user_data.email)
    if existing_user:
        raise UserAlreadyExistsException
    hashed_password = get_password_hash(user_data.password)
    await UsersDAO.add(email=user_data.email, hashed_password=hashed_password, nickname=user_data.nickname)


@router.post("/login")
async def login_user(response: Response, user_data: SUserAuth):
    user = await authenticate_user(user_data.email, user_data.password)
    if not user:
        raise IncorrectEmailOrPasswordException
    access_token = create_access_token({"sub": str(user.id)})
    response.set_cookie("todo_access_token", access_token, httponly=True)
    return {"access_token": access_token, "nickname": user.nickname}


@router.post("/logout")
async def logout_user(response: Response):
    response.delete_cookie("todo_access_token")


@router.get("/profile")
async def read_current_user(current_user: Users = Depends(get_current_user)):
    return current_user


@router.get("/all")
async def read_current_user(current_user: Users = Depends(get_current_admin_user)):
    return await UsersDAO.find_all()
