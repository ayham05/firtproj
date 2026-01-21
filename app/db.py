from sqlmodel import create_engine , SQLModel, Session 
from config import settings

sql_url = settings.sql_url

engine = create_engine(sql_url)

def creat_database_and_tables():
    SQLModel.metadata.create_all(engine)


def get_session():
    with Session(engine) as session:
        yield session
