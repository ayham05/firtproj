from pydantic import Field, EmailStr
from sqlmodel import SQLModel, Field as sqlField
from typing import Optional


class GetProduct(SQLModel):
    name:str
    description:str|None=None
    price:float = Field(gt=0, description="It must be greater than 0")
    stock:float = Field(gt=0, description="It must be greater than 0")

class Products(GetProduct, table = True):
    id: Optional[int] = sqlField(default=None, primary_key=True)
    


class GetUser(SQLModel):
    user_name: str = sqlField(unique=True)
    email: EmailStr = sqlField(unique=True)
    role: str
    hash_password: str

class Users(GetUser, table = True):
    id: Optional[int] = sqlField(default=None, primary_key=True)

