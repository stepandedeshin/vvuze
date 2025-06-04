from contextlib import asynccontextmanager

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from core.logger import app_logger as logger


@asynccontextmanager
async def fastapi_lifespan(app: FastAPI):

    logger.info('=== APP started ===')

    yield

    logger.info('=== APP stopped ===')


app = FastAPI(
    title="VVuze",
    lifespan=fastapi_lifespan
)

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