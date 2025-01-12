from datetime import datetime

from .bookmark_base import BookmarkBase


class BookmarkUpdate(BookmarkBase):
    date: datetime | None = None
    description: str | None = None
