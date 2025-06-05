from contextlib import asynccontextmanager

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from core.logger import app_logger as logger
from services.user.router import router as router_users
from services.auth.router import router as router_auth
from services.ai.router import router as router_ai
from services.chat.router import router as router_chats


@asynccontextmanager
async def fastapi_lifespan(app: FastAPI):

    logger.info('=== APP started ===')

    yield

    logger.info('=== APP stopped ===')


app = FastAPI(
    title="VVuze",
    lifespan=fastapi_lifespan
)

app.include_router(router_auth)
app.include_router(router_users)
app.include_router(router_ai)
app.include_router(router_chats)


origins = [
    "http://127.0.0.1:7000",
    "http://localhost:7000",
    "http://127.0.0.1:5432",
    "http://localhost:5432"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)