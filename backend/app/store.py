"""Temporary in-memory store for rapid iteration."""

from __future__ import annotations

from datetime import UTC, datetime
from uuid import uuid4

from .schemas import ListCreate, ListSummary


class ListStore:
    def __init__(self) -> None:
        self._lists: dict[str, ListSummary] = {}

    def create_list(self, payload: ListCreate) -> ListSummary:
        item = ListSummary(
            id=str(uuid4()),
            title=payload.title,
            description=payload.description,
            is_public=payload.is_public,
            score=0,
            created_at=datetime.now(UTC),
        )
        self._lists[item.id] = item
        return item

    def list_public(self) -> list[ListSummary]:
        public_items = [entry for entry in self._lists.values() if entry.is_public]
        return sorted(public_items, key=lambda item: item.score, reverse=True)

    def vote(self, list_id: str, direction: int) -> ListSummary | None:
        item = self._lists.get(list_id)
        if not item:
            return None
        item.score += direction
        return item


store = ListStore()
