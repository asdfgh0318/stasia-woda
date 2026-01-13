# HydraHeroes: Heroes 3 Themed Water Reminder Bot

A Telegram bot that reminds you and your friends to drink water, gamified with Heroes of Might and Magic 3 themes. Built with Python, hosted on Railway.

**Multi-user support:** Anyone who interacts with the bot automatically receives reminders!

---

## Core Features

### 1. Scheduled Water Reminders
- Automatic reminders every 2 hours (8am-10pm)
- 90+ HoMM3-themed random messages
- Creature, spell, artifact, and hero references
- **Multi-user:** All registered users receive reminders

### 2. Water Intake Logging
- `/drink` - Log a glass of water (+1)
- `/drink 3` - Log multiple glasses
- `/status` - Show today's progress

### 3. HoMM3 Gamification System

#### Hero Progression (12 Classes)
Level up based on total water logged:
```
Peasant (0)
Pikeman (10)
Archer (30)
Swordsman (60)
Griffin Rider (100)
Cavalier (175)
Crusader (275)
Champion (400)
Paladin (600)
Archangel (850)
Titan (1200)
Ancient Behemoth (2000)
```

#### Castle Building (12 Tiers)
Your castle grows with your hydration:
```
Tent (0) -> Camp (10) -> Outpost (30) -> Village (60)
-> Town (100) -> Stronghold (175) -> Castle (275)
-> Fortress (400) -> Citadel (600) -> Capitol (850)
-> Grail Temple (1200) -> Celestial Palace (2000)
```

#### Streak System (Consecutive Days)
- 3 days: Unlock "Morale Boost" badge
- 7 days: Earn "Logistics" artifact
- 14 days: Earn "Angel Wings" artifact
- 30 days: Legendary "Grail" status

#### Resources Earned
- Each glass = +10 Gold, +2 Wood, +1 Ore
- Resources displayed in castle view

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
| `/castle` | View your ASCII castle |
| `/hero` | View hero progression |
| `/leaderboard` | Hall of Heroes rankings |

---

## Setup Guide

### Step 1: Create Telegram Bot with BotFather

1. Open Telegram
2. Search for **@BotFather** (verified checkmark)
3. Click **Start** or send `/start`
4. Send `/newbot`
5. When asked for a name, enter something like:
   ```
   HydraHeroes
   ```
6. When asked for a username, enter something like:
   ```
   my_hydra_heroes_bot
   ```
   (Must end in `bot` and be unique)

7. BotFather will respond with your **bot token**:
   ```
   Use this token to access the HTTP API:
   7123456789:AAHxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
   ```
   **Save this token! It's case-sensitive!**

---

## Deployment

### Option A: Deploy to Railway (Recommended)

#### 1. Fork/Clone the repo
```bash
git clone https://github.com/asdfgh0318/stasia-woda.git
cd stasia-woda
```

#### 2. Push to your GitHub
```bash
# Create new repo on GitHub, then:
git remote set-url origin https://github.com/YOUR_USERNAME/stasia-woda.git
git push -u origin master
```

#### 3. Create Railway Project
1. Go to **https://railway.app**
2. Sign in with GitHub
3. Click **"New Project"**
4. Select **"Deploy from GitHub repo"**
5. Find and select **stasia-woda**
6. Click **"Deploy Now"**

#### 4. Add Environment Variables
1. Click on the **stasia-woda** service
2. Go to **"Variables"** tab
3. Add this variable:

| Variable | Value |
|----------|-------|
| `BOT_TOKEN` | Your token from BotFather (case-sensitive!) |

That's it! No need to configure user IDs - anyone who uses the bot will automatically receive reminders.

#### 5. Enable Metal Build (Recommended)
1. Go to **Settings** -> **Build**
2. Enable **Metal Build Environment**
3. Redeploy

#### 6. Verify Deployment
1. Go to **Deployments** tab
2. Check latest deployment shows **Success**
3. Check **Logs** tab for: `Starting HydraHeroes bot...`

### Option B: Run Locally

#### 1. Clone the repo
```bash
git clone https://github.com/asdfgh0318/stasia-woda.git
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

Edit `.env` and add your bot token:
```
BOT_TOKEN=7123456789:AAHxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
```

#### 4. Run
```bash
python bot.py
```

---

## Adding Users

Users are added automatically! Just share your bot link (`t.me/YOUR_BOT_USERNAME`) with friends. When they:
1. Open the bot and send `/start`
2. Use any command like `/drink`

They'll be registered and start receiving reminders at the scheduled times.

---

## Testing the Bot

### 1. Find Your Bot
Open Telegram and go to: `t.me/YOUR_BOT_USERNAME`

### 2. Start It
```
/start
```
You should see the welcome message.

### 3. Test Commands
```
/drink        # Log a glass, earn resources
/drink 5      # Log 5 glasses
/status       # Today's progress
/castle       # See ASCII castle art
/hero         # See all 12 hero classes
/stats        # Detailed statistics
/streak       # Streak info
```

### 4. Check Logs (if issues)
Railway -> your service -> **Logs** tab

---

## Troubleshooting

### "Invalid Token" Error
- Token is **case-sensitive** - copy exactly from BotFather
- Go to @BotFather -> `/mybots` -> select bot -> "API Token" to verify

### Bot not responding
- Check Railway logs for errors
- Verify `BOT_TOKEN` is set correctly
- Try redeploying

### Old version running
- Check Railway **Deployments** tab for latest commit hash
- If outdated, click **Redeploy** or reconnect GitHub repo

### Can't find bot in Telegram search
- New bots may take time to appear in search
- Use direct link: `t.me/YOUR_BOT_USERNAME`
- Check @BotFather -> `/mybots` for exact username

---

## Tech Stack

- **Language**: Python 3.11+
- **Bot Library**: `python-telegram-bot[job-queue]` v20+
- **Scheduler**: APScheduler (via JobQueue)
- **Database**: SQLite
- **Hosting**: Railway

---

## Project Structure

```
stasia-woda/
├── bot.py              # Main entry point
├── config.py           # Settings & environment vars
├── Dockerfile          # Container configuration
├── handlers/
│   ├── commands.py     # /drink, /status, /castle, /hero
│   ├── callbacks.py    # Button callbacks
│   └── reminders.py    # Scheduled reminder logic (multi-user)
├── game/
│   ├── progression.py  # Hero levels, XP
│   ├── streaks.py      # Streak tracking
│   ├── resources.py    # Gold, wood, ore
│   └── castle.py       # 12 castle tiers with ASCII art
├── data/
│   ├── messages.py     # 90+ reminder messages, 40+ confirmations
│   └── achievements.py # 12 hero classes, achievements
├── database/
│   ├── models.py       # SQLite schema
│   └── queries.py      # DB operations
├── requirements.txt
└── README.md
```

---

## Sample Messages

**Reminders:**
- "The Titans have spoken from their cloud temples: DRINK WATER, MORTAL."
- "The Hydra has 8 heads. You should drink 8 glasses. Coincidence?"
- "Speedrun strats: Hydration skips the 'Passing Out' cutscene."
- "Your Behemoths are getting cranky. They want you to drink water."

**Drink Confirmations:**
- "CRUSHING VICTORY! The enemy flees! +10 Gold, +2 Wood, +1 Ore!"
- "The Dragons approve! +10 Gold, +2 Wood, +1 Ore hoarded!"
- "GG EZ! +10 Gold, +2 Wood, +1 Ore in the bag!"

**Level Ups:**
- "Hill Fort upgrade: Peasant -> Pikeman! Looking sharp!"
- "The Grail's power transforms Swordsman into Crusader!"

---

## Future Enhancements

- [ ] Weekly "battle" reports
- [x] Multiple user support
- [x] Leaderboards
- [ ] Custom reminder schedules
- [ ] Image generation for castle
- [ ] Difficulty modes (reminder frequency)
