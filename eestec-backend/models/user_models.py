from sqlalchemy.orm import Mapped, mapped_column, DeclarativeBase
from sqlalchemy.sql.expression import false, true
from fastapi_users.db import SQLAlchemyUserDatabase

"""
Тут хранятся ORM (Object-Relational Mapping) модели для перевода данных о пользователе из БД
"""


"""
Базовый класс, используется в качестве основы для новых декларативных отображений
"""


class Model(DeclarativeBase):
    pass


"""
Класс для отображения пользователя в БД
"""


class UserOrm(Model):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True)
    username: Mapped[str] = mapped_column(unique=True)
    email: Mapped[str] = mapped_column(unique=True)
    hashed_password: Mapped[str] = mapped_column()
    is_active: Mapped[bool] = mapped_column(server_default=true())
    is_superuser: Mapped[bool] = mapped_column(server_default=false())
    is_verified: Mapped[bool] = mapped_column(server_default=true())
