from fastapi import FastAPI
from typing import List
from fastapi.middleware.cors import CORSMiddleware # starlette.middleware depricated
from sql_db import session # mongo DB 에서의 collection 과 같은 기능이며 database 에 access 함
from model import UserTable, User # mongoDB dml model.py 와 동일 기능임(sql 지원을 위해 조금 더 복잡함)
import uvicorn

app = FastAPI()


app.add_middleware(
    CORSMiddleware,
    allow_origins = ["*"],
    allow_credentials = True,
    allow_methods = ["*"],
    allow_headers = ["*"],
)

# 모든 db operation 은 session call로 실행함
# session operation 실행후 session.commit() 으로 마무리 함
@app.get("/users")
def read_users():
    users = session.query(UserTable).all()
    return users

@app.get("/users/{user_id}")
def read_user(user_id: str):
    user = session.query(UserTable).filter(UserTable.id == user_id).first()
    return user


@app.post("/user")
def create_user(name: str, age: int):
    user = UserTable()
    user.name = name
    user.age = age
    
    session.add(user)
    session.commit()
    return f"{name} created..."


@app.put("/users")
def update_users(users: List[User]):
    for i in users:
        user = session.query(UserTable).filter(UserTable.id == i.id).first()
        user.name = i.name
        user.age = i.age
        session.commit()
    return f"{users[0].name} updated"


@app.delete("/user")
def delete_users(user_id: int):
    print(user_id)
    user = session.query(UserTable).filter(UserTable.id == user_id).delete()
    session.commit()
    return ("deleted")

if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)