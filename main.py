import sys
import os
import config # Config'i doğrudan import et

def main():
    print("🏀 AlpiBot v1 — Environment Debug Mode\n")
    
    # Tüm ortam değişkenlerini tara (Sadece isimleri)
    print("📋 Mevcut Sistem Değişkenleri:")
    env_keys = os.environ.keys()
    for key in ["TELEGRAM_BOT_TOKEN", "TELEGRAM_CHAT_ID", "GOOGLE_AI_API_KEY", "BALLDONTLIE_API_KEY"]:
        status = "✅ BULUNDU" if key in env_keys else "❌ EKSİK!"
        print(f"  - {key}: {status}")
    
    # Config üzerinden kontrol
    print(f"\n⚙️ Config Durumu:")
    print(f"  - Telegram Token: {'Dolu' if config.TELEGRAM_BOT_TOKEN else 'BOŞ!'}")
    print(f"  - Telegram Chat ID: {'Dolu' if config.TELEGRAM_CHAT_ID else 'BOŞ!'}")

    from src.stats import get_last_game_stats, get_season_averages, get_career_totals
    from src.utils import init_db, already_tweeted, check_milestones, send_telegram_photo
    from src.ai import generate_analysis
    from src.twitter import compose_tweet
    from src.visuals import generate_stat_card

    init_db()

    try:
        game = get_last_game_stats()
        if not game: 
            print("\nℹ️ Maç verisi yok, ancak Telegram testi zorlanıyor...")
            # Test verisiyle Telegram'ı zorla (Hata varsa görmek için)
            test_game = {"matchup": "TEST vs TEST", "game_date": "Now", "pts": 0, "reb": 0, "ast": 0, "min": "0", "fg_pct": 0, "plus_minus": 0, "source": "Debug"}
            image_path = generate_stat_card(test_game)
            send_telegram_photo(image_path, caption="🧪 *AlpiBot Debug Test*\nBu mesajı görüyorsanız bağlantı başarılıdır.")
            return

        # Normal Akış...
        averages = get_season_averages()
        career = get_career_totals()
        milestones = check_milestones(career, game)
        analysis = generate_analysis(game, milestones, averages)
        tweet_text = compose_tweet(game, analysis, milestones, averages)
        image_path = generate_stat_card(game)

        caption = (
            f"🏀 *ALPEREN SENGUN | {game['matchup']}*\n📅 {game['game_date']}\n\n"
            f"⏱ {game['min']} DK  |  🏀 {game['pts']} PTS  |  💪 {game['reb']} REB\n"
            f"🅰️ {game['ast']} AST |  🛡 {game['stl']} STL  |  🚫 {game['blk']} BLK\n"
            f"✨ {analysis['tr']}"
        )

        print("\n🚀 Telegram'a gönderiliyor...")
        send_telegram_photo(image_path, caption=caption)

    except Exception as e:
        print(f"💥 Hata: {e}")

if __name__ == "__main__":
    main()
