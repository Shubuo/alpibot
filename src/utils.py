import sqlite3, json, os, requests
from datetime import datetime
from config import MILESTONE_THRESHOLDS, TELEGRAM_BOT_TOKEN, TELEGRAM_CHAT_ID

DB = "alpibot_audit.db"
JSON_DB = "alpibot_audit.json"

def init_db():
    try:
        with sqlite3.connect(DB, check_same_thread=False) as con:
            con.execute("CREATE TABLE IF NOT EXISTS tweets (id INTEGER PRIMARY KEY AUTOINCREMENT, tweet_id TEXT, game_id TEXT, game_date TEXT, pts INTEGER, reb INTEGER, ast INTEGER, tweet_text TEXT, posted_at TEXT, status TEXT)")
    except:
        if not os.path.exists(JSON_DB):
            with open(JSON_DB, 'w') as f: json.dump([], f)

def already_tweeted(game_id: str) -> bool:
    try:
        with sqlite3.connect(DB, check_same_thread=False) as con:
            return con.execute("SELECT 1 FROM tweets WHERE game_id=? AND status='success'", (game_id,)).fetchone() is not None
    except:
        if os.path.exists(JSON_DB):
            with open(JSON_DB, 'r') as f: return any(d.get("game_id") == game_id and d.get("status") == "success" for d in json.load(f))
    return False

def log_tweet(tweet_id, game: dict, tweet_text: str, status="success"):
    try:
        with sqlite3.connect(DB, check_same_thread=False) as con:
            con.execute("INSERT INTO tweets (tweet_id,game_id,game_date,pts,reb,ast,tweet_text,posted_at,status) VALUES (?,?,?,?,?,?,?,?,?)", (tweet_id, game.get("game_id"), game.get("game_date"), game.get("pts"), game.get("reb"), game.get("ast"), tweet_text, datetime.utcnow().isoformat(), status))
    except:
        data = []
        if os.path.exists(JSON_DB):
            with open(JSON_DB, 'r') as f: data = json.load(f)
        data.append({"tweet_id": tweet_id, "game_id": game.get("game_id"), "status": status})
        with open(JSON_DB, 'w') as f: json.dump(data, f)

def check_milestones(career: dict, game: dict) -> list[str]:
    milestones = []
    labels = {"pts": "kariyer sayısına", "reb": "kariyer ribounduna", "ast": "kariyer asistine"}
    for stat, thresholds in MILESTONE_THRESHOLDS.items():
        if stat in labels:
            current, prev = career[stat], career[stat] - game.get(stat, 0)
            for t in thresholds:
                if prev < t <= current: milestones.append(f"🚀 {t}. {labels[stat]} ulaştı!")
    return milestones

def get_milestone_countdown(career: dict) -> list[str]:
    countdowns = []
    labels = {"pts": "kariyer sayısına", "reb": "kariyer ribounduna", "ast": "kariyer asistine"}
    for stat, thresholds in MILESTONE_THRESHOLDS.items():
        if stat in labels:
            current = career[stat]
            next_t = next((t for t in thresholds if t > current), None)
            if next_t and (next_t - current) <= 50: countdowns.append(f"👀 {next_t} {labels[stat]} sadece {next_t - current} kaldı!")
    return countdowns

def send_telegram_photo(photo_path: str, caption: str = ""):
    if not TELEGRAM_BOT_TOKEN or not TELEGRAM_CHAT_ID: 
        print("⚠️ Telegram token veya Chat ID eksik!")
        return
    try:
        url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendPhoto"
        files = {'photo': open(photo_path, 'rb')}
        data = {'chat_id': TELEGRAM_CHAT_ID, 'caption': caption, 'parse_mode': 'Markdown'}
        resp = requests.post(url, data=data, files=files, timeout=20)
        if resp.status_code != 200:
            print(f"❌ Telegram API Hatası: {resp.status_code} - {resp.text}")
        else:
            print("✅ Telegram mesajı başarıyla gönderildi.")
    except Exception as e:
        print(f"💥 Telegram gönderim hatası: {e}")
