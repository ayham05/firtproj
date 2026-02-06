from fastapi import HTTPException, Depends, status, Response, APIRouter
from sqlmodel import select
from models import *
from db import *
from crud import get_from_db, save_to_db, delete_from_db, get_all_products, get_user_by_email, get_user_by_username, is_email_exists, is_username_exists
from crud import authenticate_user , raise_invalid_credentials
from schemas import UserCreate, UserRead, UserLogin
from core import hash_password, create_tokens , create_access_token , decode_refresh_token

router = APIRouter()




@router.get("/products")
async def all_Products(sec:Session = Depends(get_session)):
    return await get_all_products(sec)


@router.get("/users")
async def all_users(sec:Session = Depends(get_session)):
    x = select(Users)
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
    



@router.put("/register")
async def register_user(user: UserCreate, sec:Session = Depends(get_session)):

    is_username_exists(sec, user.user_name)
    is_email_exists(sec, user.email)

    hash_pass = hash_password(user.password)     
    db_user = Users(
        user_name=user.user_name,
        email=user.email,
        hash_password=hash_pass, 
        role=user.role
    )

    save_to_db(db_user,sec)


@router.post("/login")
async def login(login_data:UserLogin, sec: Session = Depends(get_session)):
    user = authenticate_user(sec, login_data.email, login_data.password)
    if not user:
        raise_invalid_credentials()
    
    access_t, refresh_t = create_tokens(user.id)
    return {
        "access_token": access_t,
        "refresh_token": refresh_t,
        "token_type": "bearer"
    }


@router.post("/refresh")
async def refresh_access_token(refresh_token: str):
    user_id = decode_refresh_token(refresh_token)
    if not user_id:
        raise_invalid_credentials
    new_token = refresh_access_token(user_id)
    return {
        "access_token": new_token,
        "token_type": "bearer"
    }