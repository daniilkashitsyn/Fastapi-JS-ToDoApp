from pydantic import BaseModel, EmailStr


class SUserAuth(BaseModel):
    email: EmailStr
    nickname: str
    password: str
