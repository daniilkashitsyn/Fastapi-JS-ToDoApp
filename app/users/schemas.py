from pydantic import BaseModel, EmailStr


class SUserAuth(BaseModel):
    email: EmailStr
    password: str


class SUserReg(BaseModel):
    email: EmailStr
    nickname: str
    password: str
