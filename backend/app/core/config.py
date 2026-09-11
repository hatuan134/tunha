from functools import lru_cache

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    app_env: str = "development"
    app_name: str = "Warehouse AI"
    api_v1_prefix: str = "/api/v1"
    app_timezone: str = "Asia/Bangkok"
    database_url: str = "postgresql+psycopg://warehouse_app:change_me_local_only@postgres:5432/warehouse_ai"
    jwt_secret: str = "replace_with_a_long_random_secret"
    jwt_algorithm: str = "HS256"
    access_token_expire_minutes: int = 30
    ai_provider: str | None = None
    ai_api_key: str | None = None

    model_config = SettingsConfigDict(env_file=".env", extra="ignore")


@lru_cache
def get_settings() -> Settings:
    return Settings()
