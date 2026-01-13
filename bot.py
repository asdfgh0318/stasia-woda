#!/usr/bin/env python3
"""HydraHeroes - A Heroes 3 themed water reminder Telegram bot."""

import logging
from telegram.ext import Application, CommandHandler

from config import BOT_TOKEN
from database import init_db
from handlers import start, help_command, drink, status, stats, streak, castle, hero
from handlers.reminders import setup_reminders

# Set up logging
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO
)
logger = logging.getLogger(__name__)


def main():
    """Start the bot."""
    # Initialize database
    init_db()

    # Check for bot token
    if not BOT_TOKEN:
        logger.error("BOT_TOKEN not set! Please set it in .env file")
        return

    # Create application
    application = Application.builder().token(BOT_TOKEN).build()

    # Add command handlers
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("help", help_command))
    application.add_handler(CommandHandler("drink", drink))
    application.add_handler(CommandHandler("status", status))
    application.add_handler(CommandHandler("stats", stats))
    application.add_handler(CommandHandler("streak", streak))
    application.add_handler(CommandHandler("castle", castle))
    application.add_handler(CommandHandler("hero", hero))

    # Set up scheduled reminders
    setup_reminders(application)

    # Start the bot
    logger.info("Starting HydraHeroes bot...")
    application.run_polling()


if __name__ == "__main__":
    main()
