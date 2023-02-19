from datetime import datetime
from pydantic import BaseModel, EmailStr, constr
from timeHelper import timeNow


class UserBaseSchema(BaseModel):
    first_name: str
    mid_name: str
    last_name: str
    phone: str
    state: str
    email: EmailStr
    badg: str | None = None
    created_at: timeNow() | None = None
    class Config:
        orm_mode = True


class CreateUserSchema(UserBaseSchema):
    password: constr(min_length=8)
    passwordConfirm: str
    verified: bool = False


class UserResponseSchema(UserBaseSchema):
    id: str
    pass


class UserResponse(BaseModel):
    status: str
    user: UserResponseSchema