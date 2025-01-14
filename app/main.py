from contextlib import asynccontextmanager

from fastapi import FastAPI
from pathlib import Path

from .database import create_db_and_tables
from .logger import configure_logger
from .routers import get_bookmarks_router


@asynccontextmanager
async def lifespan(app: FastAPI):
    base_path = Path(__file__).parent.parent
    configure_logger(base_path)

    create_db_and_tables()
    yield


app = FastAPI(lifespan=lifespan)

app.include_router(get_bookmarks_router(), prefix="/bookmarks")
