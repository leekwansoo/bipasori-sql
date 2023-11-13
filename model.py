from sqlalchemy import  Column, Integer, String
from pydantic import BaseModel
from sql_db import Base
from sql_db import engine

class UserTable(Base):
    __tablename__ = 'user'  # sqldb 에 user table 정의
    id = Column(Integer, primary_key=True, autoincrement=True, index=True)
    name = Column(String(50), nullable=False)
    age = Column(Integer)
    
class User(BaseModel):  # MongoDB model 에서의 Class User() 와 동일한 방법임
    id: int
    name: str
    age: int

# create table for User to be used for user.py
# UserTable 에서 정의된 table 생성함

def create_tables():
    Base.metadata.create_all(bind=engine)
     
create_tables()