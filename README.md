# 🏀 AlpiBot v1 — Alperen Şengün NBA Stats Tracker

AlpiBot is an automated NBA performance tracker for **Alperen Şengün**. It fetches real-time stats, generates AI-driven bilingual analysis, and creates sleek visual stat cards.

## 🚀 Features
- **Real-time Stats:** Automatic tracking via `nba_api` & `BallDontLie`.
- **AI Analysis:** Bilingual commentary powered by Google Gemini.
- **Visual Cards:** Professional PNG stat cards for every game.
- **Automation:** 24/7 autonomous operation via GitHub Actions.

## 🛠 Setup

### 1. Installation
```bash
git clone https://github.com/Shubuo/alpibot.git
pip install -r requirements.txt
```

### 2. Configuration
Create a `.env` file and provide your credentials for:
- **NBA Data:** BallDontLie API Key.
- **AI Engine:** Google AI Studio (Gemini) Key.
- **Platforms:** Twitter/X Developer Keys & Telegram Bot Token.

## 🤖 Usage
```bash
python main.py
```

## 📜 License
MIT License.
