import os
from datetime import datetime
from dotenv import load_dotenv
load_dotenv()

# ── Player & Team ──────────────────────────────────────
SENGUN_PLAYER_ID = 1630173
ROCKETS_TEAM_ID  = 1610612745
SENGUN_NAME      = "Alperen Şengün"
_y = datetime.now().year
_m = datetime.now().month
NBA_SEASON = f"{_y}-{str(_y+1)[2:]}" if _m >= 10 else f"{_y-1}-{str(_y)[2:]}"

# ── Twitter/X ──────────────────────────────────────────
TWITTER_BEARER_TOKEN        = os.getenv("TWITTER_BEARER_TOKEN", "")
TWITTER_API_KEY             = os.getenv("TWITTER_API_KEY", "")
TWITTER_API_SECRET          = os.getenv("TWITTER_API_SECRET", "")
TWITTER_ACCESS_TOKEN        = os.getenv("TWITTER_ACCESS_TOKEN", "")
TWITTER_ACCESS_TOKEN_SECRET = os.getenv("TWITTER_ACCESS_TOKEN_SECRET", "")

# ── Google Gemini ──────────────────────────────────────
GOOGLE_AI_API_KEY = os.getenv("GOOGLE_AI_API_KEY", "")
GEMINI_MODEL      = "gemini-2.0-flash"

# ── Telegram ───────────────────────────────────────────
TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN", "")
TELEGRAM_CHAT_ID   = os.getenv("TELEGRAM_CHAT_ID", "")

# ── Milestone Thresholds ───────────────────────────────
MILESTONE_THRESHOLDS = {
    "pts": [1000, 2000, 3000, 4000, 5000, 7500, 10000],
    "reb": [500, 1000, 1500, 2000, 3000, 5000],
    "ast": [300, 500, 1000, 1500, 2000],
    "blk": [150, 300, 500],
}

# ── Visuals ────────────────────────────────────────────
HASHTAGS = "#Sengun #HoustonRockets #NBATürkiye #AlpiStats"
FONT_PATH = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf" # Genelde linux sunucularda bulunur
