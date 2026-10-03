import asyncio
import logging
import os

from aiogram import Bot, Dispatcher, F, Router
from aiogram.filters import Command
from aiogram.types import Message
from dotenv import load_dotenv

load_dotenv()  # Инициализация .env

# Настройки и сис. переменные
TG_TOKEN = os.getenv("TG_TOKEN")
ADMIN_ID = int(os.getenv("ADMIN_ID"))
if not ADMIN_ID:
    raise ValueError("ADMIN_ID не установлен")

if not TG_TOKEN:
    raise ValueError("Токен бота потерялся(")

# Роутеры
dp = Dispatcher()
bot = Bot(token=TG_TOKEN)
admin_router = Router()
user_router = Router()
dp.include_router(user_router)
dp.include_router(admin_router)
logging.basicConfig(level=logging.INFO)


# Пользователь пишет /start
@user_router.message(Command("start"))
async def start_cmd(message: Message):
    await message.answer(f"Привет это кликер от @Ray474747 \n\n-Разработчики")
    logging.info(f"Пользователь {message.from_user.username} запустил бота")


# Админ пишет /start
@admin_router.message(Command("start"), F.from_user.id == ADMIN_ID)
async def start_acmd(message: Message):
    await message.answer(f"Привет, {message.from_user.username}!")
    logging.info(f"Админ {message.from_user.username} запустил бота")


# Запуск бота
async def main():
    logging.info("Запуск бота...")
    await dp.start_polling(bot)


# Запуск asyncio
if __name__ == "__main__":
    asyncio.run(main())
