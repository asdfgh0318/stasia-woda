# HydraHeroes: Heroes 3 Themed Water Reminder Bot

A Telegram bot that reminds your friend to drink water, gamified with Heroes of Might and Magic 3 themes. Built with Python, hosted on Railway/Render.

---

## Core Features

### 1. Scheduled Water Reminders
- Configurable intervals (default: every 2 hours, 8am-10pm)
- Random themed messages from a pool of HoMM3-inspired texts
- Example: *"Your troops grow weary! Restore movement points by drinking water."*

### 2. Water Intake Logging
- `/drink` - Log a glass of water (+1)
- `/drink 3` - Log multiple glasses
- `/status` - Show today's progress

### 3. HoMM3 Gamification System

#### Hero Progression
Start as a **Peasant**, level up based on total water logged:
```
Peasant (0) -> Pikeman (50) -> Swordsman (150) -> Crusader (400) -> Champion (800) -> Angel (1500)
```

#### Streak System (Consecutive Days)
- 3 days: Unlock "Morale Boost" badge
- 7 days: Earn "Logistics" artifact (+bonus message)
- 14 days: Earn "Angel Wings" artifact
- 30 days: Legendary "Grail" status

#### Daily Quests
- "Drink 8 glasses today" = Capture a gold mine
- "Log water before noon" = Ambush reward

#### Resources Earned
- Each glass = +10 Gold, +2 Wood, +1 Ore
- Weekly: "Build" castle upgrades with resources
- `/castle` - View your castle progress

### 4. Stats & Charts
- `/stats` - Daily/weekly/monthly breakdown
- `/streak` - Current streak and best streak
- `/leaderboard` - If multiple friends join

---

## Tech Stack
- **Language**: Python 3.11+
- **Bot Library**: `python-telegram-bot` v20+
- **Scheduler**: Built-in `JobQueue` from python-telegram-bot
- **Database**: SQLite (simple, no external deps)
- **Hosting**: Railway (free tier)

---

## Project Structure
```
stasia-woda/
├── bot.py              # Main bot entry point
├── handlers/
│   ├── commands.py     # /drink, /status, /stats, /castle
│   ├── callbacks.py    # Button callbacks
│   └── reminders.py    # Scheduled reminder logic
├── game/
│   ├── progression.py  # Hero levels, XP calculation
│   ├── streaks.py      # Streak tracking logic
│   ├── resources.py    # Gold, wood, ore tracking
│   └── castle.py       # Castle building system
├── data/
│   ├── messages.py     # Pool of themed reminder messages
│   └── achievements.py # Achievement definitions
├── database/
│   ├── models.py       # SQLite schema
│   └── queries.py      # DB operations
├── config.py           # Bot token, settings
├── requirements.txt
└── README.md
```

---

## Setup

### 1. Create Telegram Bot
1. Message [@BotFather](https://t.me/botfather) on Telegram
2. Send `/newbot` and follow prompts
3. Copy the bot token

### 2. Install Dependencies
```bash
pip install -r requirements.txt
```

### 3. Configure
Create a `.env` file:
```
BOT_TOKEN=your_bot_token_here
ADMIN_CHAT_ID=your_telegram_id
```

### 4. Run
```bash
python bot.py
```

---

## Deployment (Railway)

1. Push to GitHub
2. Connect repo to [Railway](https://railway.app)
3. Add environment variables (`BOT_TOKEN`, `ADMIN_CHAT_ID`)
4. Deploy!

---

## Commands

| Command | Description |
|---------|-------------|
| `/start` | Welcome message and setup |
| `/help` | Show all commands |
| `/drink [n]` | Log water intake (default: 1 glass) |
| `/status` | Today's progress and stats |
| `/stats` | Detailed statistics |
| `/streak` | Current and best streak |
| `/castle` | View your castle |
| `/hero` | View hero progression |

---

## Sample Reminder Messages

- "Your army thirsts for battle... and water! Drink now to restore movement points."
- "A wise ruler keeps their kingdom hydrated. Time for water!"
- "The Necromancers don't need water, but YOU do. Drink up!"
- "Even dragons take water breaks. Your turn, hero!"
- "Ancient wisdom says: 'He who drinks water, wins wars.' Trust the scroll."
- "Your mana is running low! Restore it with H2O."
- "Defend your health! Drink water before the enemy (dehydration) attacks."
- "+1 Morale if you drink water in the next 5 minutes!"
- "Heroes don't get dehydrated. Prove you're worthy!"
- "The Water Elementals demand tribute. One glass, please."

---

## Future Enhancements
- Weekly "battle" reports
- Multiple user support / leaderboards
- Image generation for castle visualization
- Integration with health apps
- Difficulty modes (Casual/Normal/Heroic reminder frequency)
