from fastapi import Depends

from services.auth import fastapi_users
from models.user_models import UserOrm
from schemas.user_schemas import UserReturnSchema


def get_request_actor(
    user: UserOrm = Depends(fastapi_users.current_user(active=True)),
) -> UserReturnSchema:
    """Dependency для получения исполнителя запроса
    Возвращает pydantic схему пользователя
    """
    return UserReturnSchema.model_validate(user)

