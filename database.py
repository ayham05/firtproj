from librarys import *

sqlurl = "postgresql://postgres:0159@localhost/mydb"

engine = create_engine(sqlurl)

def creatDataBase():
    SQLModel.metadata.create_all(engine)


def get_session():
    with Session(engine) as session:
        yield session
