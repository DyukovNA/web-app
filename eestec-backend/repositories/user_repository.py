from fastapi import HTTPException
from sqlalchemy import select
from utils.database import UserOrm, async_session
from schemas.user_schemas import SchemaUserAdd, SchemaUser

"""
Репозиторий используется для изменения данных в БД  

"""


class UserRepository:
    """
       Метод используется для возврата данных о пользователе по его email
       :param email: str
           String используется временно
           Желательно добавить: data_schemas.SEmail(username: str, mail_server: str, domain: str)
       :returns user: user_schemas.SUser
       """

    @classmethod
    async def get_user_by_email(cls, email: str) -> SchemaUser:
        async with async_session() as session:
            query = select(UserOrm).params(email=email).fetch(1)
            result = await session.execute(query)
            user_models = result.scalars().all()
            users = [SchemaUser.model_validate(user_model) for user_model in user_models]
            return users[0]

    """
    Метод используется для добавления пользователя в БД
    :param user: user_schemas.SUserAdd
    :returns id: int Временно
    :exception HTTPException 400 User already exists
    """
    @classmethod
    async def add_user(cls, user: SchemaUserAdd) -> bool:
        try:
            async with async_session() as session:
                data = user.model_dump()
                new_task = UserOrm(**data)

                session.add(new_task)
                await session.flush()
                await session.commit()
                return True
        except Exception as e:
            raise HTTPException(status_code=400, detail="User already exists")
