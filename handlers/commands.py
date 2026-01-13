from telegram import Update
from telegram.ext import ContextTypes

from database import get_or_create_user, log_water, get_today_glasses, get_user_stats, update_streak, add_achievement
from data.messages import get_drink_confirmation, get_level_up_message
from data.achievements import get_hero_class, get_next_hero_class
from game.progression import check_level_up, get_progress_to_next_level, get_progress_bar
from game.streaks import check_streak_achievements, get_streak_display
from game.resources import get_resources_display
from game.castle import get_castle_display
from config import GLASSES_PER_DAY_GOAL


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Handle /start command - welcome new users."""
    user = update.effective_user
    get_or_create_user(user.id, user.username)

    welcome_message = f"""
Welcome to HydraHeroes, {user.first_name}!

You are now a **Peasant** in the grand kingdom of Hydration.
Your quest: drink water, gain power, build your castle!

**How it works:**
- I'll remind you to drink water throughout the day
- Use /drink to log each glass
- Earn resources and level up your hero
- Build your castle from a humble camp to a mighty citadel!

**Commands:**
/drink - Log water intake (+1 glass)
/drink 3 - Log multiple glasses
/status - Today's progress
/stats - Detailed statistics
/streak - View your streak
/castle - See your castle
/hero - View hero progression
/help - Show all commands

Let the hydration begin!
"""
    await update.message.reply_text(welcome_message, parse_mode="Markdown")


async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Handle /help command."""
    help_text = """
**HydraHeroes Commands:**

**Hydration:**
/drink - Log 1 glass of water
/drink [n] - Log n glasses of water
/status - Today's hydration status

**Progress:**
/stats - Detailed statistics
/streak - Current and best streak
/hero - Hero class and progression
/castle - View your castle

**Info:**
/help - Show this help message

**Tips:**
- Drink 8 glasses per day for optimal hydration
- Maintain daily streaks to earn artifacts
- Each glass earns you Gold, Wood, and Ore
- Use resources to upgrade your castle!
"""
    await update.message.reply_text(help_text, parse_mode="Markdown")


async def drink(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Handle /drink command - log water intake."""
    user = update.effective_user

    # Parse number of glasses (default: 1)
    glasses = 1
    if context.args:
        try:
            glasses = int(context.args[0])
            if glasses < 1:
                glasses = 1
            elif glasses > 10:
                glasses = 10  # Cap at 10 per command
        except ValueError:
            glasses = 1

    # Get user data before logging
    user_data = get_or_create_user(user.id, user.username)
    old_total = user_data["total_glasses"]
    old_class = user_data["hero_class"]

    # Log the water
    result = log_water(user.id, glasses)
    new_total = result["total_glasses"]

    # Update streak
    streak_result = update_streak(user.id)

    # Build response message
    response = get_drink_confirmation(
        result["gold_earned"],
        result["wood_earned"],
        result["ore_earned"]
    )
    response += f"\n\n Glasses logged: {glasses}"

    # Check for first drink achievement
    if old_total == 0:
        if add_achievement(user.id, "first_drink"):
            response += "\n\n ACHIEVEMENT: First Sip!"

    # Check for level up
    level_up = check_level_up(user.id, old_total, new_total, old_class)
    if level_up:
        response += f"\n\n {get_level_up_message(level_up['old_class'], level_up['new_class'])}"

    # Check for streak achievements
    streak_achievements = check_streak_achievements(user.id, streak_result["current_streak"])
    for achievement in streak_achievements:
        response += f"\n\n {achievement['message']}"

    # Check for daily goal
    today_glasses = get_today_glasses(user.id)
    if today_glasses >= GLASSES_PER_DAY_GOAL:
        if add_achievement(user.id, "daily_goal"):
            response += "\n\n DAILY QUEST COMPLETE: Gold Mine Captured!"

    # Show today's progress
    response += f"\n\n**Today:** {today_glasses}/{GLASSES_PER_DAY_GOAL} glasses"
    response += f"\n**Streak:** {streak_result['current_streak']} days"

    await update.message.reply_text(response, parse_mode="Markdown")


async def status(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Handle /status command - show today's progress."""
    user = update.effective_user
    stats_data = get_user_stats(user.id)

    if not stats_data:
        await update.message.reply_text("Use /start to begin your hydration journey!")
        return

    progress_percent = min(100, int((stats_data["today_glasses"] / GLASSES_PER_DAY_GOAL) * 100))
    progress_bar = get_progress_bar(progress_percent)

    response = f"""
**Today's Hydration Status**

 Progress: {stats_data['today_glasses']}/{GLASSES_PER_DAY_GOAL} glasses
[{progress_bar}] {progress_percent}%

 Streak: {stats_data['current_streak']} days
 Class: {stats_data['hero_class']}

**Resources:**
{get_resources_display(stats_data['gold'], stats_data['wood'], stats_data['ore'])}

Use /drink to log water!
"""
    await update.message.reply_text(response, parse_mode="Markdown")


async def stats(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Handle /stats command - show detailed statistics."""
    user = update.effective_user
    stats_data = get_user_stats(user.id)

    if not stats_data:
        await update.message.reply_text("Use /start to begin your hydration journey!")
        return

    response = f"""
**Detailed Statistics**

**Hydration:**
 Today: {stats_data['today_glasses']} glasses
 This Week: {stats_data['week_glasses']} glasses
 This Month: {stats_data['month_glasses']} glasses
 All Time: {stats_data['total_glasses']} glasses

**Streaks:**
 Current: {stats_data['current_streak']} days
 Best: {stats_data['best_streak']} days

**Hero:**
 Class: {stats_data['hero_class']}

**Treasury:**
 Gold: {stats_data['gold']}
 Wood: {stats_data['wood']}
 Ore: {stats_data['ore']}
"""
    await update.message.reply_text(response, parse_mode="Markdown")


async def streak(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Handle /streak command - show streak information."""
    user = update.effective_user
    stats_data = get_user_stats(user.id)

    if not stats_data:
        await update.message.reply_text("Use /start to begin your hydration journey!")
        return

    streak_display = get_streak_display(
        stats_data['current_streak'],
        stats_data['best_streak']
    )

    response = f"""
**Streak Status**

{streak_display}

**Streak Rewards:**
 3 days: Morale Boost badge
 7 days: Logistics artifact
 14 days: Angel Wings artifact
 30 days: The Grail (Legendary!)
"""
    await update.message.reply_text(response, parse_mode="Markdown")


async def castle(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Handle /castle command - show castle status."""
    user = update.effective_user
    stats_data = get_user_stats(user.id)

    if not stats_data:
        await update.message.reply_text("Use /start to begin your hydration journey!")
        return

    castle_display = get_castle_display(
        stats_data['total_glasses'],
        stats_data['gold'],
        stats_data['wood'],
        stats_data['ore']
    )

    await update.message.reply_text(castle_display, parse_mode="Markdown")


async def hero(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Handle /hero command - show hero progression."""
    user = update.effective_user
    stats_data = get_user_stats(user.id)

    if not stats_data:
        await update.message.reply_text("Use /start to begin your hydration journey!")
        return

    progress = get_progress_to_next_level(stats_data['total_glasses'])
    progress_bar = get_progress_bar(progress['progress_percent'])

    response = f"""
**Hero Status**

{progress['current_icon']} **{progress['current_class']}**
Total glasses: {stats_data['total_glasses']}

"""

    if progress['next_class']:
        response += f"""**Progress to {progress['next_class']}:**
[{progress_bar}] {progress['progress_percent']}%
{progress['glasses_needed']} glasses to go!

"""
    else:
        response += "**Maximum level reached!** You are legendary!\n\n"

    response += """**Hero Classes:**
 Peasant (0 glasses)
 Pikeman (50 glasses)
 Swordsman (150 glasses)
 Crusader (400 glasses)
 Champion (800 glasses)
 Angel (1500 glasses)
"""

    await update.message.reply_text(response, parse_mode="Markdown")
