from pydantic import Field
from sqlmodel import SQLModel, Field as sqlField
from typing import Optional


class GetProduct(SQLModel):
    name:str
    description:str|None=None
    price:float = Field(gt=0, description="It must be greater than 0")
    stock:float = Field(gt=0, description="It must be greater than 0")

class Products(GetProduct, table = True):
    id: Optional[int] = sqlField(default=None, primary_key=True)
    
