ACHIEVEMENTS = {
    "first_drink": {
        "name": "First Sip",
        "description": "Log your first glass of water",
        "icon": "",
    },
    "streak_3": {
        "name": "Morale Boost",
        "description": "Maintain a 3-day hydration streak",
        "icon": "",
    },
    "streak_7": {
        "name": "Logistics",
        "description": "Maintain a 7-day hydration streak",
        "icon": "",
    },
    "streak_14": {
        "name": "Angel Wings",
        "description": "Maintain a 14-day hydration streak",
        "icon": "",
    },
    "streak_30": {
        "name": "The Grail",
        "description": "Maintain a 30-day hydration streak",
        "icon": "",
    },
    "glasses_50": {
        "name": "Pikeman",
        "description": "Log 50 total glasses of water",
        "icon": "",
    },
    "glasses_150": {
        "name": "Swordsman",
        "description": "Log 150 total glasses of water",
        "icon": "",
    },
    "glasses_400": {
        "name": "Crusader",
        "description": "Log 400 total glasses of water",
        "icon": "",
    },
    "glasses_800": {
        "name": "Champion",
        "description": "Log 800 total glasses of water",
        "icon": "",
    },
    "glasses_1500": {
        "name": "Angel",
        "description": "Log 1500 total glasses of water",
        "icon": "",
    },
    "daily_goal": {
        "name": "Gold Mine Captured",
        "description": "Reach 8 glasses in a single day",
        "icon": "",
    },
    "early_bird": {
        "name": "Ambush Victory",
        "description": "Log water before noon",
        "icon": "",
    },
}

HERO_CLASSES = [
    {"name": "Peasant", "min_glasses": 0, "icon": ""},
    {"name": "Pikeman", "min_glasses": 50, "icon": ""},
    {"name": "Swordsman", "min_glasses": 150, "icon": ""},
    {"name": "Crusader", "min_glasses": 400, "icon": ""},
    {"name": "Champion", "min_glasses": 800, "icon": ""},
    {"name": "Angel", "min_glasses": 1500, "icon": ""},
]

def get_hero_class(total_glasses: int) -> dict:
    """Get the hero class based on total glasses drunk."""
    current_class = HERO_CLASSES[0]
    for hero_class in HERO_CLASSES:
        if total_glasses >= hero_class["min_glasses"]:
            current_class = hero_class
    return current_class

def get_next_hero_class(total_glasses: int) -> dict | None:
    """Get the next hero class to unlock."""
    for hero_class in HERO_CLASSES:
        if total_glasses < hero_class["min_glasses"]:
            return hero_class
    return None
