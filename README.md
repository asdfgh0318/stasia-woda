# HydraHeroes: Heroes 3 Themed Water Reminder Bot

A Telegram bot that reminds your friend to drink water, gamified with Heroes of Might and Magic 3 themes. Built with Python, hosted on Railway.

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

## Setup Guide

### Step 1: Create Telegram Bot with BotFather

1. Open Telegram
2. Search for **@BotFather** (look for the verified checkmark)
3. Click **Start** or send `/start`
4. Send `/newbot`
5. When asked "What name do you want for your bot?", enter:
   ```
   HydraHeroes
   ```
   (This is the display name - can be anything)

6. When asked "Choose a username for your bot", enter something like:
   ```
   stasia_woda_bot
   ```
   (Must end in `bot` and be unique - try variations if taken)

7. BotFather will respond with your **bot token**:
   ```
   Use this token to access the HTTP API:
   7123456789:AAHxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
   ```
   **Save this token!**

### Step 2: Get the Recipient's Chat ID

The person who will receive reminders needs to:

1. Open Telegram
2. Search for **@userinfobot**
3. Send `/start`
4. Copy the **ID** number (e.g., `123456789`)

---

## Deployment

### Option A: Deploy to Railway (Recommended)

#### 1. Push to GitHub
```bash
git add -A
git commit -m "Update"
git push
```

#### 2. Create Railway Project
1. Go to **https://railway.app**
2. Sign in with GitHub
3. Click **"New Project"**
4. Select **"Deploy from GitHub repo"**
5. Find and select **stasia-woda**
6. Click **"Deploy Now"**

#### 3. Add Environment Variables
1. Click on the **stasia-woda** service
2. Go to **"Variables"** tab
3. Add these variables:

| Variable | Value |
|----------|-------|
| `BOT_TOKEN` | Your token from BotFather |
| `ADMIN_CHAT_ID` | Recipient's Telegram ID |

#### 4. Deploy
Railway will auto-redeploy after adding variables. If not, go to "Deployments" tab and click "Redeploy".

### Option B: Run Locally

#### 1. Clone the repo
```bash
git clone https://github.com/YOUR_USERNAME/stasia-woda.git
cd stasia-woda
```

#### 2. Create virtual environment
```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

#### 3. Configure environment
```bash
cp .env.example .env
```

Edit `.env` and add your values:
```
BOT_TOKEN=7123456789:AAHxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
ADMIN_CHAT_ID=123456789
```

#### 4. Run
```bash
python bot.py
```

---

## Testing the Bot

### 1. Find Your Bot
Open Telegram and search for your bot username (e.g., `@stasia_woda_bot`)

### 2. Start It
Send:
```
/start
```
You should see the welcome message with the Peasant introduction.

### 3. Test Core Commands

**Log water:**
```
/drink
```
(Log a glass, earn resources)

```
/drink 3
```
(Log 3 glasses at once)

**Check progress:**
```
/status
```
(See today's progress)

**View castle:**
```
/castle
```
(See your ASCII castle)

**View hero:**
```
/hero
```
(See progression to next level)

**Detailed stats:**
```
/stats
```
(Full statistics breakdown)

### 4. Check Logs (if something doesn't work)
1. Go to your Railway project
2. Click the **stasia-woda** service
3. Click **"Logs"** tab

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
├── config.py           # Bot token, settings
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
├── requirements.txt
├── railway.json        # Railway deployment config
└── README.md
```

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
