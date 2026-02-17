"""Data transfer objects for list and voting APIs."""

from datetime import datetime

from pydantic import BaseModel, Field


class ListCreate(BaseModel):
    title: str = Field(min_length=3, max_length=120)
    description: str = Field(min_length=10, max_length=1000)
    is_public: bool = True


class ListSummary(BaseModel):
    id: str
    title: str
    description: str
    is_public: bool
    score: int = 0
    created_at: datetime


class VoteCreate(BaseModel):
    direction: int = Field(ge=-1, le=1)
