import time
import tweepy
from config import (
    TWITTER_API_KEY, TWITTER_API_SECRET, TWITTER_ACCESS_TOKEN, TWITTER_ACCESS_TOKEN_SECRET, TWITTER_BEARER_TOKEN, HASHTAGS
)

def _client():
    return tweepy.Client(
        bearer_token=TWITTER_BEARER_TOKEN, consumer_key=TWITTER_API_KEY, consumer_secret=TWITTER_API_SECRET,
        access_token=TWITTER_ACCESS_TOKEN, access_token_secret=TWITTER_ACCESS_TOKEN_SECRET, wait_on_rate_limit=True,
    )

def compose_tweet(game: dict, analysis: dict, milestones: list[str], averages: dict = None) -> str:
    def get_diff(current, avg):
        diff = round(current - avg, 1)
        return f"(+{diff})" if diff > 0 else f"({diff})"
    diff_pts = get_diff(game['pts'], averages['avg_pts']) if averages else ""
    diff_reb = get_diff(game['reb'], averages['avg_reb']) if averages else ""
    result = "Galibiyetle dönüyoruz! 🏆" if game["wl"] == "W" else "Bu kez olmadı. 😤"
    ms_text = f"🚀 {' | '.join(milestones)}\n\n" if milestones else ""
    body = (
        f"Alperen Şengün vs {game['matchup'].split(' ')[-1]} 🏀\n{game['game_date']}\n\n{ms_text}"
        f"📊 {game['pts']} SAY {diff_pts} | {game['reb']} RİB {diff_reb} | {game['ast']} AST\n"
        f"✨ {game['min']} dakikada %{game['fg_pct']} isabet.\n\n{result} {analysis['tr']}\n\n{HASHTAGS}"
    )
    return body[:280]

def post_tweet(text: str) -> str:
    try:
        resp = _client().create_tweet(text=text)
        return str(resp.data["id"])
    except tweepy.TooManyRequests:
        time.sleep(60)
        resp = _client().create_tweet(text=text)
        return str(resp.data["id"])
