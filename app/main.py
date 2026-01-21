from db import *
from api.api import router
from fastapi import FastAPI
app = FastAPI()


@app.on_event("startup")
def on_startup():
    creat_database_and_tables()


app.include_router(router)

@app.get("/")
async def welcome():
    return {"message": "Welcome ZeroNero"}

