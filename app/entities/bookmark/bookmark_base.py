from datetime import datetime

from sqlmodel import SQLModel, Field


class BookmarkBase(SQLModel):
    date: datetime = Field(nullable=False)
    description: str = Field(nullable=True)
