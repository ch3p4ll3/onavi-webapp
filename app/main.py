from contextlib import asynccontextmanager

from fastapi import FastAPI
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.gzip import GZipMiddleware
from pathlib import Path

from .database import create_db_and_tables
from .logger import configure_logger
from .routers import get_bookmarks_router, get_plot_router, get_pages_router


base_path = Path(__file__).parent


@asynccontextmanager
async def lifespan(app: FastAPI):
    configure_logger(base_path.parent)

    create_db_and_tables()
    yield


templates = Jinja2Templates(directory=base_path / "www-data/templates")


app = FastAPI(lifespan=lifespan)


app.add_middleware(GZipMiddleware, minimum_size=1000)

app.include_router(get_bookmarks_router(), prefix="/bookmarks")
app.include_router(get_plot_router(), prefix="/plot")

app.mount("/static", StaticFiles(directory=base_path / "www-data/static"), name="static")
app.include_router(get_pages_router(templates))
