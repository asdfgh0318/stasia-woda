"""Castle building system based on resources accumulated."""

# Castle upgrade tiers based on total glasses (which correlates with resources)
CASTLE_TIERS = [
    {
        "name": "Camp",
        "min_glasses": 0,
        "art": """
       /\\
      /  \\
     /    \\
    /______\\
    |      |
    |  []  |
    |______|
""",
        "description": "A humble camp. Every hero starts somewhere!",
    },
    {
        "name": "Village",
        "min_glasses": 30,
        "art": """
        /\\
       /  \\
      /____\\
     /\\    /\\
    /  \\  /  \\
   /____\\/____\\
   |    ||    |
   | [] || [] |
   |____||____|
""",
        "description": "A small village grows around your camp.",
    },
    {
        "name": "Town",
        "min_glasses": 100,
        "art": """
         [_]
        /| |\\
       / | | \\
      /__|_|__\\
     |  |   |  |
    /|  | o |  |\\
   / |__|___|__| \\
  /__|         |__\\
  |  | [] | [] |  |
  |__|____|____|__|
""",
        "description": "Your settlement has grown into a proper town!",
    },
    {
        "name": "Castle",
        "min_glasses": 250,
        "art": """
     [###]     [###]
      |=|       |=|
   ___|=|_______|=|___
  |   |=|       |=|   |
  |   |=|  ___  |=|   |
  |___|=|_|   |_|=|___|
  |   | |  o  | |   |
  | o | |     | | o |
  |___|_|_____|_|___|
""",
        "description": "A mighty castle stands as testament to your dedication!",
    },
    {
        "name": "Fortress",
        "min_glasses": 500,
        "art": """
    [###]         [###]
     |=|    ___    |=|
   __|=|___/   \\___|=|__
  |  |=|  | (*) |  |=|  |
  |  |=|  |     |  |=|  |
  |__|=|__|     |__|=|__|
  |     | |     | |     |
  |  o  | |  o  | |  o  |
  |_____|_|_____|_|_____|
""",
        "description": "An imposing fortress! Your enemies tremble!",
    },
    {
        "name": "Citadel",
        "min_glasses": 1000,
        "art": """
        [###]       [###]
    [###]|=|  ___  |=|[###]
     |=| |=| /   \\ |=| |=|
   __|=|_|=|| *** ||=|_|=|__
  |  |=| |=||     ||=| |=|  |
  |__|=|_|=||_____||=|_|=|__|
  |     |    | |    |     |
  |  o  |  o | | o  |  o  |
  |_____|____|_|____|_____|
""",
        "description": "A legendary citadel! Songs are sung of your hydration prowess!",
    },
]


def get_castle_tier(total_glasses: int) -> dict:
    """Get the current castle tier based on total glasses."""
    current_tier = CASTLE_TIERS[0]
    for tier in CASTLE_TIERS:
        if total_glasses >= tier["min_glasses"]:
            current_tier = tier
    return current_tier


def get_next_castle_tier(total_glasses: int) -> dict | None:
    """Get the next castle tier to unlock."""
    for tier in CASTLE_TIERS:
        if total_glasses < tier["min_glasses"]:
            return tier
    return None


def get_castle_display(total_glasses: int, gold: int, wood: int, ore: int) -> str:
    """Generate the full castle display with stats."""
    current = get_castle_tier(total_glasses)
    next_tier = get_next_castle_tier(total_glasses)

    display = f"=== {current['name']} ===\n"
    display += f"```{current['art']}```\n"
    display += f"_{current['description']}_\n\n"
    display += f"**Treasury:**\n"
    display += f" Gold: {gold}\n"
    display += f" Wood: {wood}\n"
    display += f" Ore: {ore}\n\n"

    if next_tier:
        glasses_needed = next_tier["min_glasses"] - total_glasses
        display += f"**Next upgrade:** {next_tier['name']}\n"
        display += f"Glasses needed: {glasses_needed}"
    else:
        display += "**Maximum level reached!** Your citadel is legendary!"

    return display
