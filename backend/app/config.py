"""Runtime configuration for the API."""

from pydantic import BaseModel
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file='.env', env_prefix='LISTRANK_')

    app_name: str = 'ListRank API'
    firebase_project_id: str | None = None
    firebase_storage_bucket: str | None = None


class HealthResponse(BaseModel):
    status: str
    service: str


settings = Settings()
