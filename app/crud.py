from fastapi import HTTPException, Depends, status, Response, APIRouter
from sqlmodel import select
from models import *
from db import *
from core import verify_password


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

def get_user_by_email(session: Session, email: str):
    return session.exec(select(Users).where(Users.email == email)).first()

def get_user_by_username(session: Session, user_name: str):
    return session.exec(select(Users).where(Users.user_name == user_name)).first()

def is_email_exists(sec: Session, email: str):
    
    if get_user_by_email(sec, email):
        raise HTTPException(
                status_code=400, 
                detail="email is exists"
            )


def is_username_exists(sec: Session, username: str):
    
    if get_user_by_username(sec, username):
        raise HTTPException(
                status_code=400, 
                detail="email is exists"
            )


def authenticate_user(session: Session, email: str, password: str) -> Optional[Users]:
    user = get_user_by_email(session, email)
    if not user:
        return None
    
    if not verify_password(password, user.hash_password):
        return None
        
    return user


def raise_invalid_credentials():
    raise HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="email or password not existe",
        headers={"WWW-Authenticate": "Bearer"},
    )
