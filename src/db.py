from motor.motor_asyncio import AsyncIOMotorClient

from src.config import get_settings


settings = get_settings()
client = AsyncIOMotorClient(host=settings.MONGO_HOST,
                            port=settings.MONGO_PORT)
