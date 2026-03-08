from PIL import Image, ImageDraw, ImageFont
import os

def generate_stat_card(game: dict, output_path="stat_card.png"):
    w, h = 1200, 675
    bg_color = (10, 10, 10)
    accent = (206, 17, 65) 
    white = (255, 255, 255)
    gray = (160, 160, 160)
    img = Image.new('RGB', (w, h), color=bg_color)
    draw = ImageDraw.Draw(img)
    draw.rectangle([0, 0, 15, h], fill=accent)
    font_paths = ["/System/Library/Fonts/Supplemental/Arial.ttf", "/Library/Fonts/Arial Unicode.ttf", "DejaVuSans.ttf"]
    def get_font(size):
        for path in font_paths:
            try: return ImageFont.truetype(path, size)
            except: continue
        return ImageFont.load_default()
    f_player, f_name, f_title, f_sub, f_stat, f_label = get_font(25), get_font(40), get_font(90), get_font(30), get_font(130), get_font(25)
    draw.text((80, 50), "PLAYER", fill=accent, font=f_player)
    draw.text((80, 85), "ALPEREN SENGUN", fill=white, font=f_name)
    draw.text((80, 180), "MATCH STATS", fill=accent, font=f_title)
    draw.text((80, 280), f"{game['matchup']}  |  {game['game_date']}", fill=gray, font=f_sub)
    stats = [{"val": str(game['pts']), "lbl": "PTS", "x": 80}, {"val": str(game['reb']), "lbl": "REB", "x": 350}, {"val": str(game['ast']), "lbl": "AST", "x": 650}, {"val": str(game.get('eff', '-')), "lbl": "EFF", "x": 950}]
    for item in stats:
        draw.text((item['x'], 380), item['val'], fill=white, font=f_stat)
        draw.text((item['x'], 530), item['lbl'], fill=accent, font=f_label)
        draw.line([item['x'], 565, item['x']+80, 565], fill=accent, width=4)
    draw.rectangle([0, h-60, w, h], fill=(25, 25, 25))
    footer_text = f"MIN: {game['min']}  |  FG: %{game['fg_pct']}  |  +/-: {game['plus_minus']}  |  AlpiBot v1"
    draw.text((80, h-45), footer_text, fill=gray, font=f_label)
    img.save(output_path)
    return output_path
