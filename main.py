import sys
import os
import config
from src.stats import get_last_game_stats, get_career_totals, get_season_averages
from src.utils import init_db, already_tweeted, log_tweet, check_milestones, send_telegram_photo
from src.ai import generate_analysis
from src.twitter import compose_tweet, post_tweet
from src.visuals import generate_stat_card

def main():
    print("🏀 AlpiBot v1 — Houston Rockets Edition\n")
    init_db()

    try:
        game = get_last_game_stats()
        if not game: 
            print("ℹ️ Yeni maç verisi yok.")
            return

        if already_tweeted(game["game_id"]):
            print(f"ℹ️ {game['game_id']} zaten paylaşıldı.")
            return

        averages = get_season_averages()
        career = get_career_totals()
        milestones = check_milestones(career, game)
        analysis = generate_analysis(game, milestones, averages)
        tweet_text = compose_tweet(game, analysis, milestones, averages)
        image_path = generate_stat_card(game)

        # Telegram Zengin & Kompakt Altyazı
        caption = (
            f"🏀 *ALPEREN SENGUN | {game['matchup']}*\n"
            f"📅 {game['game_date']}\n\n"
            f"⏱ {game['min']} DK  |  🏀 {game['pts']} PTS  |  💪 {game['reb']} REB\n"
            f"🅰️ {game['ast']} AST |  🛡 {game['stl']} STL  |  🚫 {game['blk']} BLK\n"
            f"🎯 FG2: {game['fg2']}  |  FG3: {game['fg3']}  |  FT: {game['ft']}\n"
            f"⚠️ TO: {game['tov']}  |  📉 PF: {game['pf']}  |  📊 +/-: {game['plus_minus']}\n\n"
            f"✨ {analysis['tr']}"
        )

        print(f"📱 REPORT:\n{caption}\n")

        # Twitter ve Telegram Paylaşımı
        if os.getenv("TWITTER_API_KEY") and os.getenv("TWITTER_ACCESS_TOKEN"):
            print("🚀 Canlı mod: Twitter ve Telegram'a gönderiliyor...")
            try:
                tweet_id = post_tweet(tweet_text)
                log_tweet(tweet_id, game, tweet_text, status="success")
                send_telegram_photo(image_path, caption=f"✅ *TWEETED!*\n\n{caption}")
            except Exception as e:
                print(f"❌ Twitter hatası: {e}")
                send_telegram_photo(image_path, caption=f"❌ *Twitter Hatası!*\n\n{caption}")
        else:
            print("🧪 Dry-run: Sadece Telegram'a gönderiliyor...")
            send_telegram_photo(image_path, caption=caption)

    except Exception as e:
        print(f"💥 Hata: {e}")

if __name__ == "__main__":
    main()
