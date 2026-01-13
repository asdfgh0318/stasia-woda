"""Castle building system based on resources accumulated."""

# Castle upgrade tiers based on total glasses (which correlates with resources)
CASTLE_TIERS = [
    {
        "name": "Tent",
        "min_glasses": 0,
        "art": """
        ⛺
       /  \\
      /    \\
     /______\\
""",
        "description": "A lonely tent. Every legend begins with a single step...",
    },
    {
        "name": "Camp",
        "min_glasses": 10,
        "art": """
       /\\     🔥
      /  \\   /|\\
     /    \\
    /______\\  ⛺
    |      |
    |  []  |
    |______|
""",
        "description": "A humble camp with a fire. Home sweet home!",
    },
    {
        "name": "Outpost",
        "min_glasses": 30,
        "art": """
      [⚑]
       |
      /|\\
     / | \\
    /__|__\\
    |     |
    | ▓▓▓ |
    |_____|___
    |    ⌂   |
    |________|
""",
        "description": "A watchtower rises! Your domain expands.",
    },
    {
        "name": "Village",
        "min_glasses": 60,
        "art": """
        /\\
       /  \\    /\\
      /____\\  /__\\
     /\\    /\\ |  |
    /  \\  /  \\|__|
   /____\\/____\\
   |    ||    | ♠♠
   | [] || [] |♠♠♠
   |____||____|
""",
        "description": "A village forms! Peasants gather under your banner.",
    },
    {
        "name": "Town",
        "min_glasses": 100,
        "art": """
         [⚑]
        /| |\\
       / | | \\    /\\
      /__|_|__\\  /  \\
     |  |   |  |/____\\
    /|  | ☼ |  |    |
   / |__|___|__| [] |
  /__|         |____|
  |  | [] | [] |  |
  |__|____|____|__|
""",
        "description": "A proper town with a market square!",
    },
    {
        "name": "Stronghold",
        "min_glasses": 175,
        "art": """
     ║▓▓▓║     ║▓▓▓║
     ║   ║     ║   ║
   ══╩═══╩═════╩═══╩══
   ║                 ║
   ║    ┌─────┐      ║
   ║    │ ▓▓▓ │      ║
   ║    │     │      ║
   ╠════╧═════╧══════╣
   ║  ▓  │ ⌂ │  ▓    ║
   ╚═════╧═══╧═══════╝
""",
        "description": "Stone walls rise! Raiders dare not approach.",
    },
    {
        "name": "Castle",
        "min_glasses": 275,
        "art": """
     [⚔]         [⚔]
      ║           ║
   ╔══╩═══════════╩══╗
   ║  ╔═══════════╗  ║
   ║  ║           ║  ║
   ║  ║   ┌───┐   ║  ║
   ║  ║   │ ♔ │   ║  ║
   ╠══╬═══╧═══╧═══╬══╣
   ║▓▓║  ▓  ⌂  ▓  ║▓▓║
   ╚══╩═══════════╩══╝
""",
        "description": "A castle worthy of a king! The throne awaits.",
    },
    {
        "name": "Fortress",
        "min_glasses": 400,
        "art": """
    ╔═══╗         ╔═══╗
    ║ ⚔ ║   ⛨    ║ ⚔ ║
   ═╩═══╩═════════╩═══╩═
   ║ ╔═══════════════╗ ║
   ║ ║   ╔═══════╗   ║ ║
   ║ ║   ║ ◆ ♔ ◆ ║   ║ ║
   ║ ║   ╚═══════╝   ║ ║
   ╠═╬═══════════════╬═╣
   ║▓║ ▓ │ ▓ ⌂ ▓ │ ▓ ║▓║
   ╚═╩═══╧═══════╧═══╩═╝
""",
        "description": "An imposing fortress! Armies rally to your cause.",
    },
    {
        "name": "Citadel",
        "min_glasses": 600,
        "art": """
       ╔═══╗     ╔═══╗
    ╔══╣ ⚜ ╠═════╣ ⚜ ╠══╗
    ║  ╚═══╝ ⛨⛨⛨ ╚═══╝  ║
   ═╩══════════════════════╩═
   ║  ╔════════════════╗   ║
   ║  ║  ╔══════════╗  ║   ║
   ║  ║  ║  ♔ 👑 ♕  ║  ║   ║
   ║  ║  ╚══════════╝  ║   ║
   ╠══╬════════════════╬═══╣
   ║▓▓║ ▓ ▓ │ ⌂⌂⌂ │ ▓ ▓║▓▓║
   ╚══╩═════╧═════╧════╩══╝
""",
        "description": "A legendary citadel! Bards sing of your glory!",
    },
    {
        "name": "Capitol",
        "min_glasses": 850,
        "art": """
            ╔═══════╗
            ║  ✧✧✧  ║
       ╔════╬═══════╬════╗
       ║ ⚜ ║   ⛨   ║ ⚜ ║
   ════╩════╩═══════╩════╩════
   ║   ╔════════════════╗    ║
   ║   ║  ╔══════════╗  ║    ║
   ║   ║  ║ 👑 ♔♕ 👑 ║  ║    ║
   ║   ║  ╚══════════╝  ║    ║
   ╠═══╬════════════════╬════╣
   ║▓▓▓║ ▓▓ │ ⌂⌂⌂⌂ │ ▓▓ ║▓▓▓║
   ╚═══╩════╧══════╧════╩═══╝
""",
        "description": "The Capitol! Seat of an empire! Nations bow before you!",
    },
    {
        "name": "Grail Temple",
        "min_glasses": 1200,
        "art": """
              ☀️
            ╱╲
           ╱  ╲
          ╱ 🏆 ╲
         ╱══════╲
        ╔════════════╗
   ═════╬════════════╬═════
   ║ ⚜ ║     ✨     ║ ⚜ ║
   ║   ╠════════════╣   ║
   ║   ║ 👑 ♔ ⚱ ♕ 👑║   ║
   ╠═══╬════════════╬═══╣
   ║▓▓▓║ ▓▓▓ ⌂⌂ ▓▓▓ ║▓▓▓║
   ╚═══╩════════════╩═══╝
""",
        "description": "THE GRAIL TEMPLE! Ultimate power achieved! You are IMMORTAL!",
    },
    {
        "name": "Celestial Palace",
        "min_glasses": 2000,
        "art": """
           ✨ ☀️ ✨
          ╱ 🌟🌟🌟 ╲
         ╱    🏆    ╲
        ╱ ═══════════ ╲
   ════╬═══════════════╬════
   ║ 👼 ║   ✨ ⛨ ✨   ║ 👼 ║
   ║   ╠═══════════════╣   ║
   ║   ║  👑 ♔⚱♕ 👑   ║   ║
   ║   ║   ═══════     ║   ║
   ╠═══╬═══════════════╬═══╣
   ║▓▓▓║▓▓▓ ⌂⌂⌂⌂⌂ ▓▓▓ ║▓▓▓║
   ╚═══╩═══════════════╩═══╝
       ☁️           ☁️
""",
        "description": "CELESTIAL PALACE! You have transcended mortality! The Angels themselves kneel!",
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
