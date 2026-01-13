from data.achievements import HERO_CLASSES, get_hero_class, get_next_hero_class
from database.queries import update_hero_class


def check_level_up(telegram_id: int, old_total: int, new_total: int, current_class: str) -> dict | None:
    """Check if user leveled up and return new class info if they did."""
    old_class_info = get_hero_class(old_total)
    new_class_info = get_hero_class(new_total)

    if new_class_info["name"] != old_class_info["name"]:
        # Level up occurred!
        update_hero_class(telegram_id, new_class_info["name"])
        return {
            "old_class": old_class_info["name"],
            "new_class": new_class_info["name"],
            "new_icon": new_class_info["icon"],
        }

    return None


def get_progress_to_next_level(total_glasses: int) -> dict:
    """Get progress information towards next level."""
    current = get_hero_class(total_glasses)
    next_class = get_next_hero_class(total_glasses)

    if next_class is None:
        return {
            "current_class": current["name"],
            "current_icon": current["icon"],
            "next_class": None,
            "glasses_needed": 0,
            "progress_percent": 100,
        }

    # Find the previous threshold
    prev_threshold = current["min_glasses"]
    next_threshold = next_class["min_glasses"]

    glasses_in_level = total_glasses - prev_threshold
    glasses_for_level = next_threshold - prev_threshold
    progress_percent = int((glasses_in_level / glasses_for_level) * 100)

    return {
        "current_class": current["name"],
        "current_icon": current["icon"],
        "next_class": next_class["name"],
        "next_icon": next_class["icon"],
        "glasses_needed": next_threshold - total_glasses,
        "progress_percent": progress_percent,
    }


def get_progress_bar(percent: int, length: int = 10) -> str:
    """Generate a text-based progress bar."""
    filled = int(length * percent / 100)
    empty = length - filled
    return "" * filled + "" * empty
