import hashlib
import os

from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
from collections.abc import AsyncGenerator
from sqlalchemy.ext.asyncio import AsyncSession

from models.user_models import UserOrm, Model

"""
Создание engine и sessionmaker.
"""


engine = create_async_engine(os.getenv('DATABASE_URL'))
async_session = async_sessionmaker(engine, expire_on_commit=False)


"""
Методы для проверки работоспособности БД
"""


async def create_tables():
    async with engine.begin() as conn:
        await conn.run_sync(Model.metadata.create_all)


async def delete_tables():
    async with engine.begin() as conn:
        await conn.run_sync(Model.metadata.drop_all)


async def test_tables():
    async with async_session() as session:
        password = "dfghj"
        hashed = hashlib.md5(password.encode())
        session.add(UserOrm(username="User1", email="email", hashed_password=hashed.hexdigest()))
        await session.flush()
        await session.commit()


async def get_async_session() -> AsyncGenerator[AsyncSession, None]:
    """
    A coroutine that asynchronously yields an AsyncSession object.
    """

    async with async_session() as session:
        yield session
