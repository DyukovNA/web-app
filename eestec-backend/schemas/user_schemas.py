from pydantic import BaseModel, ConfigDict

"""
Pydantic позволяет создавать JSON схемы из моделей. Модели пользователей приведены ниже
"""

"""
Используется для возврата id пользователя
:param BaseModel Наследует BaseModel
"""


class UserIdSchema(BaseModel):
    id: int


"""
Используется для возврата данных о пользователе
:param BaseModel Наследует BaseModel
"""


class UserReturnSchema(BaseModel):
    username: str
    email: str

    model_config = ConfigDict(from_attributes=True)


"""
Используется при регистрации. Добавляется поле названное hased_password, 
хотя при регистрации передаётся пароль без хешрования и становится защищённым позже
:param SUserReturn Наследует SUserReturn
"""


class SchemaUserAdd(UserReturnSchema):
    hashed_password: str

    model_config = ConfigDict(from_attributes=True)


"""
Используется для передачи полной информации о пользователе из БД
:param SUserAdd Наследует SUserAdd
"""


class SchemaUser(SchemaUserAdd):  # Почему пароль в схеме?
    id: int

    model_config = ConfigDict(from_attributes=True)
