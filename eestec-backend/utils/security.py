import hashlib
import os
from datetime import datetime, timedelta

import jwt

from schemas.user_schemas import SchemaUserAdd

"""
Хеширует пароль, возвращает такого же пользователя, но с защищённым паролем для записи в БД
"""


def encrypt(user_init: SchemaUserAdd) -> SchemaUserAdd:
    hashed = hashlib.md5(user_init.hashed_password.encode())
    user = SchemaUserAdd(
        username=user_init.username,
        email=user_init.email,
        hashed_password=hashed.hexdigest()
    )
    return user


"""
Создаёт JWT (JSON Web Token) по email
"""


def create_token(email: str):
    pass
    # TODO
