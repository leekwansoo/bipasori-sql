# sqlalchemy: python 으로 sql database 관리하는 module (sql database 언어로 변환하여 줌) 
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, scoped_session

SQL_DATABASE_URL = "sqlite:///./user.db"  
# accessing sqlite3 embedded in fastapi instead using mysql
# file root directory 에 user.db 가 만들어져 있음

# db engine 생성
engine = create_engine(
    SQL_DATABASE_URL,
    )

# session 생성 (MongoDB 에서 collection 과 같은 역활)
session = scoped_session(
    sessionmaker(
        autocommit=False,
        autoflush=False,
        bind=engine    
    )
)

# 
Base = declarative_base()
Base.query = session.query_property()