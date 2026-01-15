from librarys import *

counter : int = 100

class get_Product(SQLModel):
    name:str
    description:str|None=None
    price:float = Field(gt=0, description="It must be greater than 0")
    stock:float = Field(gt=0, description="It must be greater than 0")

class Products(SQLModel, table = True):
    id :int = sqlField(default=None, primary_key=True)
    name:str
    description:str|None=None
    price:float = Field(gt=0, description="It must be greater than 0")
    stock:float = Field(gt=0, description="It must be greater than 0")
    def __init__(self, oth:get_Product):
        global counter
        self.id = counter
        counter = counter + 1
        self.name = oth.name
        self.price = oth.price
        self.stock = oth.stock
        self.description = oth.description
