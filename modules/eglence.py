import json
import os
import random
import threading
import time
from telegram import Bot

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(BASE_DIR, "..", "data")

DOSYALAR = {
    "espri": os.path.join(DATA_DIR, "espriler.json"),
    "fıkra": os.path.join(DATA_DIR, "fıkralar.json"),
    "muzik": os.path.join(DATA_DIR, "muzikler.json"),
    "gorsel": os.path.join(DATA_DIR, "gorseller.json")
}

CHAT_ID = -1002520321072  # Genel grup chat_id


def rastgele_sec(dosya_yolu):
    try:
        with open(dosya_yolu, "r", encoding="utf-8") as f:
            liste = json.load(f)
            return random.choice(liste) if liste else None
    except:
        return None


def icerik_gonder(bot: Bot):
    secim = random.choice(["espri", "fıkra", "muzik", "gorsel"])
    veri = rastgele_sec(DOSYALAR[secim])

    if not veri:
        return

    if secim == "muzik":
        bot.send_message(chat_id=CHAT_ID, text=f"🎵 Rastgele müzik önerisi: {muzik_link}")

    elif secim == "espri":
        bot.send_message(chat_id=CHAT_ID, text=f"😂 {veri}")
    elif secim == "fıkra":
        bot.send_message(chat_id=CHAT_ID, text=f"🗯️ Fıkra zamanı:\n\n{fikra}")

    elif secim == "gorsel":
        bot.send_photo(chat_id=CHAT_ID, photo=veri)


def zamanlayici_baslat(bot: Bot):
    def dongu():
        while True:
            time.sleep(1 * 60)  # 15 dakika
            icerik_gonder(bot)

    threading.Thread(target=dongu, daemon=True).start()
