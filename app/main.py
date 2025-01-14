from contextlib import asynccontextmanager

from fastapi import FastAPI
from fastapi.middleware.gzip import GZipMiddleware
from pathlib import Path

from .database import create_db_and_tables
from .logger import configure_logger
from .routers import get_bookmarks_router, get_plot_router


@asynccontextmanager
async def lifespan(app: FastAPI):
    base_path = Path(__file__).parent.parent
    configure_logger(base_path)

    create_db_and_tables()
    yield


app = FastAPI(lifespan=lifespan)

app.add_middleware(GZipMiddleware, minimum_size=1000)

app.include_router(get_bookmarks_router(), prefix="/bookmarks")
app.include_router(get_plot_router(), prefix="/plot")
