from librarys import *


class get_product(SQLModel):
    name:str
    description:str|None=None
    price:float = Field(gt=0, description="It must be greater than 0")
    stock:float = Field(gt=0, description="It must be greater than 0")

class Products(get_product, table = True):
    id: Optional[int] = Field(default=None, primary_key=True)
    
