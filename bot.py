import asyncio
import logging

from aiogram import Bot, Dispatcher
from config import TG_TOKEN
from database import init_db
from handlers import admin_router, user_router


async def main():
    logging.basicConfig(level=logging.INFO)
    logging.info("Запуск бота...")

    bot = Bot(token=TG_TOKEN)
    dp = Dispatcher()
    dp.include_router(admin_router)
    dp.include_router(user_router)

    await dp.start_polling(bot)


if __name__ == "__main__":
    init_db()
    asyncio.run(main())
