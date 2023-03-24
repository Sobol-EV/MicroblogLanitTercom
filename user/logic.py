from fastapi_users.authentication import JWTAuthentication
from fastapi_users.db import SQLAlchemyUserDatabase
from core.db import database
from .models import User
from .schemas import UserDB, UserCreate
from .models import get_user_db
from fastapi_users import BaseUserManager, FastAPIUsers
from typing import Optional
from fastapi import Depends, Request


users = User.__table__
user_db = SQLAlchemyUserDatabase(UserDB, database, users)

SECRET = "dhfg67ewtf8wgf6ewgc8y28g8q893hc7808fwh7w4bynw74y7"

auth_backends = [
    JWTAuthentication(secret=SECRET, lifetime_seconds=3600),
]

class UserManager(BaseUserManager[UserCreate, UserDB]):
  user_db_model = UserDB
  reset_password_token_secret = SECRET
  verification_token_secret = SECRET

  async def on_after_register(self, user: UserDB, request: Optional[Request] = None):
    print(f"User {user.id} has registered.")


  async def on_after_forgot_password(self, user: UserDB, token: str, request: Optional[Request] = None):
    print(f"User {user.id} has forgot their password. Reset token: {token}")


  async def on_after_request_verify(self, user: UserDB, token: str, request: Optional[Request] = None):
    print(f"Verification requested for user {user.id}. Verification token: {token}")


def get_user_manager(user_db: SQLAlchemyUserDatabase = Depends(get_user_db)):
  yield UserManager(user_db)


jwt_authentication = JWTAuthentication(
    secret=SECRET, lifetime_seconds=3600, tokenUrl="auth/jwt/login"
)
