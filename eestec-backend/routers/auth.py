from services.auth import fastapi_users, auth_backend
from dependencies import get_request_actor
from schemas.auth import AuthUserGetSchema, AuthRegisterSchema
from schemas.user_schemas import UserReturnSchema
from fastapi import APIRouter, Depends


router = APIRouter(
    prefix="/api",
    tags=["API"],
)

router.include_router(fastapi_users.get_auth_router(auth_backend))
router.include_router(
    fastapi_users.get_register_router(AuthUserGetSchema, AuthRegisterSchema),
)
router.include_router(
    fastapi_users.get_verify_router(AuthUserGetSchema),
)


@router.get(
    "/me",
    response_model=UserReturnSchema
)
async def get_me(
    actor: UserReturnSchema = Depends(get_request_actor)
):
    return actor
