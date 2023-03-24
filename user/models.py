from fastapi_users.db import SQLAlchemyBaseUserTable, SQLAlchemyUserDatabase
from sqlalchemy import Column, String, Integer, DateTime, Boolean
from core.db import Base, database
from .schemas import UserDB
import databases
import sqlalchemy

class User(Base, SQLAlchemyBaseUserTable):
    name = Column(String, unique=True)
    date = Column(DateTime)


users = User.__table__


def get_user_db():
    yield SQLAlchemyUserDatabase(UserDB, database, users)
