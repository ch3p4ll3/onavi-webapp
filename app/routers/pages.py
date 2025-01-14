from typing import Annotated

from fastapi import APIRouter, Request, Depends
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from sqlmodel import Session

from ..database import get_session

from ..entities.bookmark.bookmark import Bookmark


def get_router(template: Jinja2Templates):
    router = APIRouter()

    @router.get("/", name="index", response_class=HTMLResponse)
    async def root(request: Request):
        return template.TemplateResponse(
            request=request, name="index.html"
        )
    
    @router.get("/bookmarks", name="bookmarks", response_class=HTMLResponse)
    async def bookmarks(request: Request, db: Annotated[Session, Depends(get_session)]):
        bookmarks = Bookmark.get_all(db)
        
        return template.TemplateResponse(
            request=request, name="bookmarks.html",
            context={
                "bookmarks": bookmarks
            }
        )

    return router
