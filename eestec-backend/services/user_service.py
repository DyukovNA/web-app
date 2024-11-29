from fastapi import Depends

from repositories.user_repository import UserRepository
from schemas.user_schemas import SchemaUserAdd, SchemaUser
from utils.security import encrypt

"""
Сервис содержит методы для работы с репозиторией user_repository
"""

"""
Добавляет пользователя в БД, возвращает запись из БД о пользователе
"""


async def add_user(user_init: SchemaUserAdd = Depends()) -> SchemaUser:
    user_to_add = encrypt(user_init)
    if await UserRepository.add_user(user_to_add):
        new_user = await UserRepository.get_user_by_email(user_to_add.email)
        return new_user
    else:
        return None
