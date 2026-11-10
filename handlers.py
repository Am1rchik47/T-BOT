import logging

from aiogram import F, Router
from aiogram.filters import Command
from aiogram.types import Message
from config import ADMIN_ID
from database import add_user, get_user

user_router = Router()
admin_router = Router()


@user_router.message(Command("start"))
async def start_cmd(message: Message):
    add_user(message.from_user.id, message.from_user.username)
    await message.answer(f"{message.from_user.first_name}, добро пожаловать в Clicker!")
    logging.info(f"Пользователь {message.from_user.username} запустил бота")


@user_router.message(Command("menu"))
async def menu_cmd(message: Message):
    user = get_user(message.from_user.id)
    if user is None:
        await message.answer("Сначала напишите /start")
        return

    _, _, balance, exp, level, _ = user
    await message.answer(
        f"--- Кликер ---\n"
        f"Имя: {message.from_user.first_name}\n"
        f"Баланс: {balance}\n"
        f"Опыт: {exp}\n"
        f"Уровень: {level}"
    )
    logging.info(f"Пользователь {message.from_user.username} вызвал меню")


@admin_router.message(Command("admin"), F.from_user.id == ADMIN_ID)
async def admin_cmd(message: Message):
    await message.answer(
        f"--- Админ панель ---\n"
        f"Имя: {message.from_user.first_name}\n"
        f"ID: {message.from_user.id}\n"
        f"Статистика:\nСкоро..."
    )
    logging.info(f"Админ {message.from_user.username} открыл админ-панель")
