from fastapi_users import schemas
from pydantic import BaseModel, ConfigDict


class AuthUserGetSchema(schemas.BaseUser[int]):
    username: str


class AuthRegisterSchema(schemas.BaseUserCreate):
    username: str

