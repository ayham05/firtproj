from fastapi import HTTPException, Depends, status, Response, APIRouter
from sqlmodel import select
from models import *
from db import *


async def get_all_products(db:Session):
    x = select(Products)
    ret = db.exec(x).all() 
    return ret

async def get_from_db(id:int, sec: Session):
    ret = sec.get(Products, id)
    if not ret:
        raise HTTPException(status_code = 404, detail = "NOT FOUND")
        return {"Messege":"ERROR"}
    else:
        return ret
    

def save_to_db(pp:Products, sec:Session):
    sec.add(pp)
    sec.commit()
    sec.refresh(pp)


def delete_from_db(pp:Products, sec:Session):
    sec.delete(pp)
    sec.commit()