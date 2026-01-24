from passlib.context import CryptContext
from datetime import datetime , timedelta, timezone
from jose import jwt
from config import settings

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto", bcrypt__truncate_error=True)

SECRET_KEY = settings.SECRET_KEY
ALGORITHM = settings.ALGORITHM
ACCESS_TOKEN_EXPIRE_MINUTES = 30
REFRESH_TOKEN_EXPIRE_DAYS = 7

def hash_password(password:str)->str:
    return pwd_context.hash(password)

def create_tokens(id:int):
    access_expire = datetime.now(timezone.utc) + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = jwt.encode({"sub": str(id), "exp": access_expire}, SECRET_KEY, algorithm=ALGORITHM)

    refresh_expire = datetime.now(timezone.utc) + timedelta(days=REFRESH_TOKEN_EXPIRE_DAYS)
    refresh_token = jwt.encode({"sub": str(id), "exp": refresh_expire}, SECRET_KEY, algorithm=ALGORITHM)

    return access_token, refresh_token



def verify_password(plain_password: str, hashed_password: str) ->bool:
    return pwd_context.verify(plain_password, hashed_password)
