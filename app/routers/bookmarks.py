from typing import Annotated, List

from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session

from ..database import get_session

from ..entities.bookmark.bookmark_public import BookmarkPublic
from ..entities.bookmark.bookmark_create import BookmarkCreate
from ..entities.bookmark.bookmark_update import BookmarkUpdate
from ..entities.bookmark.bookmark import Bookmark


def get_router():
    router = APIRouter()

    @router.get("/", response_model=List[BookmarkPublic])
    async def get_all_bookmarks(db: Annotated[Session, Depends(get_session)]):
        return Bookmark.get_all(db=db)

    @router.get("/{id}", response_model=BookmarkPublic)
    async def get_bookmark_by_id(id: int, db: Annotated[Session, Depends(get_session)]):
        bookmark = Bookmark.get_by_id(bookmark_id=id, db=db)

        if bookmark is None:
            raise HTTPException(status_code=404, detail="Bookmark not found")
        return bookmark

    @router.post("/", response_model=BookmarkPublic)
    async def create_bookmark(bookmark: BookmarkCreate, db: Annotated[Session, Depends(get_session)]):
        bookmark = Bookmark(**bookmark.model_dump())

        return Bookmark.create(bookmark=bookmark, db=db)

    @router.put("/{id}", response_model=BookmarkPublic)
    async def update_bookmark(id: int, bookmark: BookmarkUpdate, db: Annotated[Session, Depends(get_session)]):
        bookmark = Bookmark.update(bookmark_id=id, bookmark=bookmark, db=db)

        if bookmark is None:
            raise HTTPException(status_code=404, detail="Bookmark not found")
        return bookmark

    @router.delete("/{id}", response_model=bool)
    async def delete_bookmark(id: int, db: Annotated[Session, Depends(get_session)]):
        is_deleted = Bookmark.delete(bookmark_id=id, db=db)

        if not is_deleted:
            raise HTTPException(status_code=404, detail="Bookmark not found")
        return is_deleted

    return router
