import asyncio
import os

from aiogram import Bot, Dispatcher, F, Router
from aiogram.filters import Command
from aiogram.types import Message
from dotenv import load_dotenv

load_dotenv()  # Инициализация .env

# Настройки и сис. переменные
TG_TOKEN = os.getenv(TG_TOKEN)
if not TG_TOKEN:
    raise ValueError("Токен бота потерялся(")
dp = Dispatcher()
bot = Bot(token=TG_TOKEN)
router = Router()
dp.include_router(router)


@router.message(Command("start"))
async def start_cmd():
    await message.answer(f"Привет это кликер от @Ray474747 \n\n-Разработчики")


async def main():
    dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main)
