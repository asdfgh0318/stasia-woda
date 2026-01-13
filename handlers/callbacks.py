"""Callback handlers for inline buttons (future use)."""

from telegram import Update
from telegram.ext import ContextTypes


async def button_callback(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Handle button callbacks."""
    query = update.callback_query
    await query.answer()

    # Future: handle quick drink buttons, etc.
    data = query.data

    if data == "quick_drink":
        # Could trigger the drink logic here
        await query.edit_message_text("Use /drink to log water!")
