import uuid
from typing import Optional
import jwt
from os import getenv

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from sqlalchemy.orm import selectinload

from fastapi import Depends, Request
from fastapi_users import BaseUserManager, IntegerIDMixin
from fastapi_users import FastAPIUsers
from fastapi_users.authentication import (
    AuthenticationBackend,
    BearerTransport,
    JWTStrategy,
)
from fastapi_users.db import SQLAlchemyUserDatabase

from models.user_models import UserOrm as User
from utils.database import get_async_session

bearer_transport = BearerTransport(tokenUrl="/api/login")


class UserManager(IntegerIDMixin, BaseUserManager[User, int]):
    """Класс для управления моделью пользователя в контексте авторизации
    :param reset_password_token_secret: str
        Ключ для шифрования токена сброса пароля
    :param verification_token_secret: str
        Ключ для шифрования токена доступа
    """
    reset_password_token_secret = getenv("SECRET_KEY", 'replaceme')
    verification_token_secret = getenv("SECRET_KEY", 'replaceme')


class _AuthUserModel(SQLAlchemyUserDatabase):
    """Класс для взаимодействияя с бд"""
    pass


def get_jwt_strategy() -> JWTStrategy:
    """Стратегия передачи данных о токене"""
    return JWTStrategy(secret=getenv("SECRET_KEY", "replaceme"), lifetime_seconds=3600)


async def _get_user_db(session: AsyncSession = Depends(get_async_session)):
    """Dependency для получения класса для работы с пользователями"""
    yield _AuthUserModel(session, User)


async def _get_user_manager(user_db: SQLAlchemyUserDatabase = Depends(_get_user_db)):
    yield UserManager(user_db)


auth_backend = AuthenticationBackend(
    name="jwt",
    transport=bearer_transport,
    get_strategy=get_jwt_strategy,
)
# Используется как контроллер модуля авторизации

fastapi_users = FastAPIUsers[User, int](_get_user_manager, [auth_backend])
# Верхнеуровневое взаимодейтсвие с модудем авторизации
