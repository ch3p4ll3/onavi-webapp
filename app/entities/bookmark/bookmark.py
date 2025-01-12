from typing import Union

from sqlmodel import Field, Session, select
from .bookmark_base import BookmarkBase

class Bookmark(BookmarkBase, table=True):
    id: int | None = Field(default=None, primary_key=True)

    @classmethod
    def get_all(cls, db: Session) -> list["Bookmark"]:
        bookmarks = db.exec(select(cls)).all()

        return list(bookmarks)

    @classmethod
    def get_by_id(cls, db: Session, bookmark_id: int) -> Union["Bookmark", None]:
        bookmark = db.get(cls, bookmark_id)

        return bookmark

    @classmethod
    def create(cls, db: Session, bookmark: "Bookmark") -> "Bookmark":
        db_location = cls.model_validate(bookmark)
        db.add(db_location)
        db.commit()
        db.refresh(db_location)

        return db_location

    @classmethod
    def update(cls, db: Session, bookmark_id: int, bookmark: "Bookmark") -> Union["Bookmark", None]:
        db_bookmark = db.get(cls, bookmark_id)
        if not db_bookmark:
            return

        hero_data = bookmark.model_dump(exclude_unset=True)
        db_bookmark.sqlmodel_update(hero_data)
        db.add(db_bookmark)
        db.commit()
        db.refresh(db_bookmark)

        return db_bookmark

    @classmethod
    def delete(cls, db: Session, bookmark_id: int) -> bool:
        db_location = db.get(cls, bookmark_id)

        if not db_location:
            return False

        db.delete(db_location)
        db.commit()

        return True

    @classmethod
    def delete_all(cls, db: Session):
        db_locations = db.exec(select(cls)).all()

        for vendor in db_locations:
            db.delete(vendor)
        db.commit()
