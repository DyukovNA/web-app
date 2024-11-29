from contextlib import asynccontextmanager

import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from utils.database import create_tables, delete_tables, test_tables
from routers.user_router import router as user_router
from routers.auth import router as auth_router


"""
Создание и удаления таблиц для упрощения разработки
"""


@asynccontextmanager
async def lifespan(app: FastAPI):
    await create_tables()
    await test_tables()
    print("База готова")
    yield
    await delete_tables()
    print("База очищена")


app = FastAPI(lifespan=lifespan)

origins = [
    "http://localhost:5049",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins="*",
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(user_router)
app.include_router(auth_router)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=5049)