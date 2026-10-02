import os

from aiogram import Bot, Dispatcher
from dotenv import load_dotenv

load_dotenv()  # Инициализация .env

# Настройки и сис. переменные
TG_TOKEN = os.getenv(TG_TOKEN)
if not TG_TOKEN:
    raise ValueError("Токен бота потерялся(")
dp = Dispatcher()
bot = Bot(token=TG_TOKEN)
