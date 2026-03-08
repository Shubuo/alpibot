import json
from google import genai
from google.genai import types
from config import GOOGLE_AI_API_KEY, GEMINI_MODEL

client = genai.Client(api_key=GOOGLE_AI_API_KEY)

def generate_analysis(game_stats: dict, milestones: list[str], averages: dict = None) -> dict:
    try:
        avg_str = f"\nSeason Averages: {json.dumps(averages)}" if averages else ""
        prompt = f"Sen bir NBA analistisin. Maçı izlemediğini unutma, nesnel verilere odaklan. Oyun: {json.dumps(game_stats)}{avg_str}. Önce TR 1-2 cümle, sonra ' -- ', sonra EN karşılığı. Maks 160 karakter."
        response = client.models.generate_content(model=GEMINI_MODEL, contents=prompt, config=types.GenerateContentConfig(max_output_tokens=200, temperature=0.7))
        text = response.text.strip().replace("**", "").replace("*", "").replace("#", "")
        if " -- " in text:
            tr, en = text.split(" -- ", 1)
            return {"tr": tr.strip(), "en": en.strip()}
        return {"tr": text, "en": ""}
    except:
        return {"tr": "İstatistiksel olarak istikrarlı bir performans. Alperen takımına katkı vermeye devam ediyor.", "en": "Statistically consistent performance. Alpi continues to contribute."}
