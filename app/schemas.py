from sqlmodel import SQLModel
from pydantic import EmailStr, Field, BaseModel


class UserBase(SQLModel):
    user_name: str = Field(unique = True, index = True)
    email: EmailStr = Field(unique = True, index = True)
    role: str = "user"

class UserCreate(UserBase):
    password: str = Field(min_length=8)

class UserRead(UserBase):
    id: int


class UserLogin(BaseModel):
    email: EmailStr
    password: str

 