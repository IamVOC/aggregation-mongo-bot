from pydantic_settings import BaseSettings, SettingsConfigDict
from functools import lru_cache


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file='.env',
                                      env_file_encoding='utf-8')

    MONGO_HOST: str
    MONGO_PORT: int
    MONGO_NAME: str
    MONGO_COLL: str
    TOKEN: str


@lru_cache
def get_settings() -> Settings:
    return Settings()
