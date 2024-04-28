import asyncio
from aiogram import Bot, Dispatcher

from src.config import get_settings
from src.routers.default_router import default_router


async def main():
    settings = get_settings()

    bot = Bot(token=settings.TOKEN)
    dp = Dispatcher()

    dp.include_router(default_router)

    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())
