from data.messages import STREAK_MESSAGES
from database.queries import add_achievement


STREAK_MILESTONES = [3, 7, 14, 30]


def check_streak_achievements(telegram_id: int, current_streak: int) -> list:
    """Check and award streak achievements. Returns list of newly earned achievements."""
    new_achievements = []

    for milestone in STREAK_MILESTONES:
        if current_streak >= milestone:
            achievement_id = f"streak_{milestone}"
            if add_achievement(telegram_id, achievement_id):
                new_achievements.append({
                    "id": achievement_id,
                    "message": STREAK_MESSAGES.get(milestone, f"{milestone}-day streak achieved!"),
                })

    return new_achievements


def get_streak_display(current_streak: int, best_streak: int) -> str:
    """Generate a display string for streak information."""
    # Find next milestone
    next_milestone = None
    for milestone in STREAK_MILESTONES:
        if current_streak < milestone:
            next_milestone = milestone
            break

    display = f"Current Streak: {current_streak} days\n"
    display += f"Best Streak: {best_streak} days\n"

    if next_milestone:
        days_to_go = next_milestone - current_streak
        display += f"\nNext milestone: {next_milestone} days ({days_to_go} to go!)"
    else:
        display += "\nYou've reached all streak milestones! Legendary!"

    return display
