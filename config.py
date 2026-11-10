import os

from dotenv import load_dotenv

load_dotenv()

TG_TOKEN = os.getenv("TG_TOKEN")
ADMIN_ID_STR = os.getenv("ADMIN_ID")

if not TG_TOKEN:
    raise ValueError("Токен бота (TG_TOKEN) не установлен в .env")
if not ADMIN_ID_STR:
    raise ValueError("ADMIN_ID не установлен в .env")

ADMIN_ID = int(ADMIN_ID_STR)
DB_PATH = "clicker.db"
