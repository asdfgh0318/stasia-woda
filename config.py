import os
from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")
ADMIN_CHAT_ID = os.getenv("ADMIN_CHAT_ID")

# Reminder settings
REMINDER_INTERVAL_HOURS = 2
REMINDER_START_HOUR = 8  # 8 AM
REMINDER_END_HOUR = 22   # 10 PM

# Database - use /data for Railway persistent volume, fallback to local for development
DATABASE_PATH = os.getenv("DATABASE_PATH", "/data/hydra_heroes.db" if os.path.exists("/data") else "hydra_heroes.db")

# Game settings
GLASSES_PER_DAY_GOAL = 8
GOLD_PER_GLASS = 10
WOOD_PER_GLASS = 2
ORE_PER_GLASS = 1
