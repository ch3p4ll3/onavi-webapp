from contextlib import asynccontextmanager

from fastapi import FastAPI
from pathlib import Path

from .database import create_db_and_tables
from .routers import get_bookmarks_router


base_path = Path(__file__).parent


@asynccontextmanager
async def lifespan(app: FastAPI):
    create_db_and_tables()
    yield


app = FastAPI(lifespan=lifespan)

app.include_router(get_bookmarks_router(), prefix="/bookmarks")
