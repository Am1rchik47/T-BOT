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
admin_router.filter(F.from_user.id == ADMIN_ID)


# Пользователь пишет /start
@user_router.message(Command("start"))
async def start_cmd(message: Message):
    await message.answer(
        f"--- Кликер ---\n"
        f"Имя: {message.from_user.first_name}\n"
        f"Баланс: Скоро...\n"
        f"Опыт: Скоро..."
    )
    logging.info(f"Пользователь {message.from_user.username} запустил бота")


# Админ пишет /admin
@admin_router.message(Command("admin"))
async def start_acmd(message: Message):
    await message.answer(
        f"--- Админ панель ---\n"
        f"Имя: {message.from_user.first_name}\n"
        f"ID: {message.from_user.id}\n"
        f"Игроки: Скоро..."
        f"Статистика: Скоро..."
    )
    logging.info(f"Админ {message.from_user.username} открыл панель администратора")


# Запуск бота
async def main():
    logging.info("Запуск бота...")
    await dp.start_polling(bot)


# Запуск asyncio
if __name__ == "__main__":
    asyncio.run(main())
