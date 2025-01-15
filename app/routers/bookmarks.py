from typing import Annotated, List

from datetime import datetime
from io import BytesIO

from fastapi import APIRouter, Depends, HTTPException, UploadFile, Form
from sqlmodel import Session

from ..database import get_session

from ..entities.bookmark.bookmark_public import BookmarkPublic
from ..entities.bookmark.bookmark_create import BookmarkCreate
from ..entities.bookmark.bookmark_update import BookmarkUpdate
from ..entities.bookmark.bookmark import Bookmark

from ..helpers.utils import Utils
from ..helpers.influx_helper import InfluxHelper


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

    @router.delete("/{id}", response_model=bool, name="bookmark_delete")
    async def delete_bookmark(id: int, db: Annotated[Session, Depends(get_session)]):
        is_deleted = Bookmark.delete(bookmark_id=id, db=db)

        if not is_deleted:
            raise HTTPException(status_code=404, detail="Bookmark not found")
        return is_deleted
    
    @router.post("/import")
    async def import_from_csv(csv_file: UploadFile, event_time: Annotated[datetime, Form()], description: Annotated[str, Form()], db: Annotated[Session, Depends(get_session)]):
        file_like_object = BytesIO(await csv_file.read())
        file_like_object.name = csv_file.filename

        measurements = await Utils.import_csv_file(file_like_object)

        # write to influx retention bucket
        await InfluxHelper.write_influx(measurements)

        # create bookmark
        bookmark = Bookmark(
            date=event_time,
            description=description
        )
        Bookmark.create(db, bookmark)

    return router
