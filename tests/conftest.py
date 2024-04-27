import pytest
from motor.motor_asyncio import AsyncIOMotorClient

from src.config import get_settings

pytest_plugins = ('pytest_asyncio',)


@pytest.fixture()
def setup_motor():
    settings = get_settings()
    client = AsyncIOMotorClient(host=settings.MONGO_HOST,
                                port=settings.MONGO_PORT)
    coll = client[settings.MONGO_NAME][settings.MONGO_COLL]
    yield coll
