"""List ranking API entrypoint."""

from fastapi import FastAPI, HTTPException

from .config import HealthResponse, settings
from .firebase import init_firebase
from .schemas import ListCreate, ListSummary, VoteCreate
from .store import store

app = FastAPI(title=settings.app_name)


@app.on_event('startup')
def startup() -> None:
    init_firebase()


@app.get('/health', response_model=HealthResponse)
def health() -> HealthResponse:
    return HealthResponse(status='ok', service=settings.app_name)


@app.get('/lists', response_model=list[ListSummary])
def get_public_lists() -> list[ListSummary]:
    return store.list_public()


@app.post('/lists', response_model=ListSummary, status_code=201)
def create_list(payload: ListCreate) -> ListSummary:
    return store.create_list(payload)


@app.post('/lists/{list_id}/vote', response_model=ListSummary)
def vote_on_list(list_id: str, payload: VoteCreate) -> ListSummary:
    updated = store.vote(list_id=list_id, direction=payload.direction)
    if not updated:
        raise HTTPException(status_code=404, detail='List not found')
    return updated
