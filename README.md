# 🏀 AlpiBot v1 — Alperen Şengün NBA Stats Tracker

AlpiBot is an automated Twitter (X) and Telegram bot that tracks **Alperen Şengün's** NBA performance. It fetches real-time stats, performs AI-driven bilingual analysis, tracks career milestones, and generates visual stat cards.

## 🚀 Features

-   **Real-time Data:** Fetches latest game stats via `nba_api` with a robust fallback to `BallDontLie API`.
-   **AI Analysis:** Generates objective, bilingual (Turkish & English) commentary using **Google Gemini 1.5/2.0 Flash**.
-   **Smart Comparison:** Automatically compares game stats with current season averages.
-   **Visual Stat Cards:** Generates sleek, high-quality PNG images for every game.
-   **Milestone Tracking:** Monitors career thresholds (Points, Rebounds, Assists) and provides "countdown" alerts.
-   **Automated Workflow:** Runs 24/7 using GitHub Actions.
-   **Multi-Platform:** Posts to Twitter and sends status reports to Telegram.

## 🛠 Installation

### 1. Clone the repository
```bash
git clone https://github.com/Shubuo/alpibot.git
cd alpibot
```

### 2. Install dependencies
```bash
pip install -r requirements.txt
```

### 3. Configuration
Create a `.env` file in the root directory and add your API keys for the following platforms:
- **Google AI Studio:** (Gemini API)
- **BallDontLie:** (NBA Stats Backup)
- **Twitter/X Developer:** (Posting - Optional)
- **Telegram Bot:** (Notifications - Optional)

## 🤖 Usage

### Manual Run
```bash
python main.py
```

### Automation (GitHub Actions)
The project includes a pre-configured workflow in `.github/workflows/alpibot.yml`. To enable it:
1.  Go to your GitHub Repository **Settings > Secrets and variables > Actions**.
2.  Add all keys from your `.env` as **Repository Secrets**.
3.  The bot will automatically check for games 3 times a day (07:00, 10:00, 13:00 TRT).

## 📊 Sample Output (Tweet Style)
> Alperen Şengün vs SAS 🏀
> Mar 08, 2026
>
> 📊 28 SAY (+6.4) | 12 RİB (+3.0) | 5 AST
> ✨ 32 dakikada %75.0 isabetle gelen performans!
>
> Galibiyetle dönüyoruz! 🏆 Müthiş bir verimlilik ve istikrarlı performans.
>
> #Sengun #HoustonRockets #NBATürkiye

## 🤝 Contributing
Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📜 License
Distributed under the MIT License. See `LICENSE` for more information.
