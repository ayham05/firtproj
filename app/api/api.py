from fastapi import HTTPException, Depends, status, Response, APIRouter
from sqlmodel import select
from schemas import *
from dp import *
from .endpoints import get_from_db, save_to_db, delete_from_db

router = APIRouter()

@router.get("/products")
async def all_Products(sec:Session = Depends(get_session)):
    x = select(Products)
    ret = sec.exec(x).all() 
    return ret


@router.get("/item/{id}")
async def get_item(id:int, sec : Session = Depends(get_session)):
    ret = await get_from_db(id, sec)
    return ret


@router.post("/products", status_code=status.HTTP_201_CREATED)
async def create_item(f:GetProduct, sec:Session = Depends(get_session)):
    pp:Products = Products.model_validate(f)
    save_to_db(pp,sec)
    return pp 


@router.put("/products/{id}")
async def update_item(id:int ,f:GetProduct, sec:Session = Depends(get_session)):
    x = await get_from_db(id,sec)
    x.sqlmodel_update(f)
    save_to_db(x,sec)
    return x
    

@router.delete("/products/{id}")
async def delete_item(id:int , sec:Session = Depends(get_session)):
    x = await get_from_db(id,sec)
    delete_from_db(x,sec)
    return {"messege":"item deleted"}
    