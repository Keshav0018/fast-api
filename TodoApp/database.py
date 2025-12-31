from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

SQLALCHEMY_DATABASE_URL = (
    "postgresql://todo_db_0i7e_user:zwxfiUBnXFCHfbhZO7CRESX4el81IT9k@dpg-d5an2amr433s738gr0og-a/todo_db_0i7e"
)

engine = create_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()