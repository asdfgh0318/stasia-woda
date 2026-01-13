import sqlite3
from datetime import date, datetime, timedelta
from database.models import get_connection
from config import GOLD_PER_GLASS, WOOD_PER_GLASS, ORE_PER_GLASS


def get_or_create_user(telegram_id: int, username: str = None) -> dict:
    """Get existing user or create a new one."""
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM users WHERE telegram_id = ?", (telegram_id,))
    row = cursor.fetchone()

    if row:
        user = {
            "telegram_id": row[0],
            "username": row[1],
            "hero_class": row[2],
            "total_glasses": row[3],
            "gold": row[4],
            "wood": row[5],
            "ore": row[6],
            "current_streak": row[7],
            "best_streak": row[8],
            "last_drink_date": row[9],
            "created_at": row[10],
        }
    else:
        cursor.execute(
            "INSERT INTO users (telegram_id, username) VALUES (?, ?)",
            (telegram_id, username)
        )
        conn.commit()
        user = {
            "telegram_id": telegram_id,
            "username": username,
            "hero_class": "Peasant",
            "total_glasses": 0,
            "gold": 0,
            "wood": 0,
            "ore": 0,
            "current_streak": 0,
            "best_streak": 0,
            "last_drink_date": None,
            "created_at": datetime.now().isoformat(),
        }

    conn.close()
    return user


def log_water(telegram_id: int, glasses: int = 1) -> dict:
    """Log water intake and update user stats. Returns updated user data."""
    conn = get_connection()
    cursor = conn.cursor()

    # Insert water log
    cursor.execute(
        "INSERT INTO water_logs (telegram_id, glasses) VALUES (?, ?)",
        (telegram_id, glasses)
    )

    # Calculate resources earned
    gold_earned = glasses * GOLD_PER_GLASS
    wood_earned = glasses * WOOD_PER_GLASS
    ore_earned = glasses * ORE_PER_GLASS

    # Update user stats
    cursor.execute("""
        UPDATE users SET
            total_glasses = total_glasses + ?,
            gold = gold + ?,
            wood = wood + ?,
            ore = ore + ?,
            last_drink_date = ?
        WHERE telegram_id = ?
    """, (glasses, gold_earned, wood_earned, ore_earned, date.today().isoformat(), telegram_id))

    conn.commit()

    # Get updated user data
    cursor.execute("SELECT * FROM users WHERE telegram_id = ?", (telegram_id,))
    row = cursor.fetchone()
    conn.close()

    return {
        "telegram_id": row[0],
        "username": row[1],
        "hero_class": row[2],
        "total_glasses": row[3],
        "gold": row[4],
        "wood": row[5],
        "ore": row[6],
        "current_streak": row[7],
        "best_streak": row[8],
        "last_drink_date": row[9],
        "glasses_logged": glasses,
        "gold_earned": gold_earned,
        "wood_earned": wood_earned,
        "ore_earned": ore_earned,
    }


def get_today_glasses(telegram_id: int) -> int:
    """Get the number of glasses logged today."""
    conn = get_connection()
    cursor = conn.cursor()

    today = date.today().isoformat()
    cursor.execute("""
        SELECT COALESCE(SUM(glasses), 0) FROM water_logs
        WHERE telegram_id = ? AND DATE(logged_at) = ?
    """, (telegram_id, today))

    result = cursor.fetchone()[0]
    conn.close()
    return result


def get_user_stats(telegram_id: int) -> dict:
    """Get comprehensive user statistics."""
    conn = get_connection()
    cursor = conn.cursor()

    # Get user data
    cursor.execute("SELECT * FROM users WHERE telegram_id = ?", (telegram_id,))
    row = cursor.fetchone()

    if not row:
        conn.close()
        return None

    # Get today's glasses
    today = date.today().isoformat()
    cursor.execute("""
        SELECT COALESCE(SUM(glasses), 0) FROM water_logs
        WHERE telegram_id = ? AND DATE(logged_at) = ?
    """, (telegram_id, today))
    today_glasses = cursor.fetchone()[0]

    # Get this week's glasses
    week_start = (date.today() - timedelta(days=date.today().weekday())).isoformat()
    cursor.execute("""
        SELECT COALESCE(SUM(glasses), 0) FROM water_logs
        WHERE telegram_id = ? AND DATE(logged_at) >= ?
    """, (telegram_id, week_start))
    week_glasses = cursor.fetchone()[0]

    # Get this month's glasses
    month_start = date.today().replace(day=1).isoformat()
    cursor.execute("""
        SELECT COALESCE(SUM(glasses), 0) FROM water_logs
        WHERE telegram_id = ? AND DATE(logged_at) >= ?
    """, (telegram_id, month_start))
    month_glasses = cursor.fetchone()[0]

    conn.close()

    return {
        "telegram_id": row[0],
        "username": row[1],
        "hero_class": row[2],
        "total_glasses": row[3],
        "gold": row[4],
        "wood": row[5],
        "ore": row[6],
        "current_streak": row[7],
        "best_streak": row[8],
        "last_drink_date": row[9],
        "today_glasses": today_glasses,
        "week_glasses": week_glasses,
        "month_glasses": month_glasses,
    }


def update_streak(telegram_id: int) -> dict:
    """Update user's streak based on consecutive drinking days."""
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT last_drink_date, current_streak, best_streak FROM users WHERE telegram_id = ?", (telegram_id,))
    row = cursor.fetchone()

    if not row:
        conn.close()
        return {"current_streak": 0, "best_streak": 0, "streak_increased": False}

    last_drink_date_str, current_streak, best_streak = row
    today = date.today()
    streak_increased = False

    if last_drink_date_str:
        last_drink_date = date.fromisoformat(last_drink_date_str)
        days_diff = (today - last_drink_date).days

        if days_diff == 0:
            # Same day, no streak change
            pass
        elif days_diff == 1:
            # Consecutive day, increase streak
            current_streak += 1
            streak_increased = True
            if current_streak > best_streak:
                best_streak = current_streak
        else:
            # Streak broken, reset to 1
            current_streak = 1
            streak_increased = True
    else:
        # First time drinking
        current_streak = 1
        best_streak = 1
        streak_increased = True

    cursor.execute("""
        UPDATE users SET current_streak = ?, best_streak = ? WHERE telegram_id = ?
    """, (current_streak, best_streak, telegram_id))

    conn.commit()
    conn.close()

    return {
        "current_streak": current_streak,
        "best_streak": best_streak,
        "streak_increased": streak_increased,
    }


def add_achievement(telegram_id: int, achievement_id: str) -> bool:
    """Add an achievement for a user. Returns True if newly earned."""
    conn = get_connection()
    cursor = conn.cursor()

    try:
        cursor.execute(
            "INSERT INTO user_achievements (telegram_id, achievement_id) VALUES (?, ?)",
            (telegram_id, achievement_id)
        )
        conn.commit()
        conn.close()
        return True
    except sqlite3.IntegrityError:
        # Already has this achievement
        conn.close()
        return False


def get_user_achievements(telegram_id: int) -> list:
    """Get all achievements for a user."""
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        "SELECT achievement_id, earned_at FROM user_achievements WHERE telegram_id = ?",
        (telegram_id,)
    )
    achievements = cursor.fetchall()
    conn.close()

    return [{"id": a[0], "earned_at": a[1]} for a in achievements]


def update_hero_class(telegram_id: int, hero_class: str):
    """Update user's hero class."""
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("UPDATE users SET hero_class = ? WHERE telegram_id = ?", (hero_class, telegram_id))
    conn.commit()
    conn.close()


def get_all_users() -> list:
    """Get all registered users (for broadcasting reminders)."""
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT telegram_id FROM users")
    users = [row[0] for row in cursor.fetchall()]
    conn.close()
    return users


def get_leaderboard(limit: int = 10) -> list:
    """Get top users by total glasses for leaderboard."""
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        SELECT telegram_id, username, hero_class, total_glasses, current_streak, best_streak
        FROM users
        ORDER BY total_glasses DESC
        LIMIT ?
    """, (limit,))
    rows = cursor.fetchall()
    conn.close()

    return [
        {
            "telegram_id": row[0],
            "username": row[1],
            "hero_class": row[2],
            "total_glasses": row[3],
            "current_streak": row[4],
            "best_streak": row[5],
        }
        for row in rows
    ]
