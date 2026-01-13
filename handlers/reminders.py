"""Scheduled reminder functionality."""

from datetime import time
from telegram.ext import Application, ContextTypes

from data.messages import get_random_reminder
from config import REMINDER_INTERVAL_HOURS, REMINDER_START_HOUR, REMINDER_END_HOUR
from database.queries import get_all_users


async def send_reminder(context: ContextTypes.DEFAULT_TYPE):
    """Send a water reminder to all registered users."""
    users = get_all_users()

    if not users:
        print("No users registered, skipping reminder")
        return

    message = get_random_reminder()
    reminder_text = f"{message}\n\nUse /drink to log your water!"

    sent_count = 0
    for user_id in users:
        try:
            await context.bot.send_message(
                chat_id=user_id,
                text=reminder_text
            )
            sent_count += 1
        except Exception as e:
            print(f"Failed to send reminder to {user_id}: {e}")

    print(f"Reminder sent to {sent_count}/{len(users)} users")


def setup_reminders(application: Application):
    """Set up scheduled water reminders."""
    job_queue = application.job_queue

    if job_queue is None:
        print("Warning: JobQueue not available. Install with: pip install 'python-telegram-bot[job-queue]'")
        print("Reminders disabled - bot will still work for commands.")
        return

    # Schedule reminders every REMINDER_INTERVAL_HOURS during active hours
    for hour in range(REMINDER_START_HOUR, REMINDER_END_HOUR, REMINDER_INTERVAL_HOURS):
        reminder_time = time(hour=hour, minute=0)
        job_queue.run_daily(
            send_reminder,
            time=reminder_time,
            name=f"water_reminder_{hour}"
        )
        print(f"Scheduled reminder at {reminder_time}")

    print(f"Reminders configured: every {REMINDER_INTERVAL_HOURS}h from {REMINDER_START_HOUR}:00 to {REMINDER_END_HOUR}:00")
