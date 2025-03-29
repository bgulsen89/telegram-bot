from telegram import Update
from telegram.ext import CallbackContext, CommandHandler, MessageHandler, Filters
import json
import os
from datetime import datetime

DATA_PATH = "data/onayli_uyeler.json"

def load_onayli_uyeler():
    if not os.path.exists(DATA_PATH):
        return []
    with open(DATA_PATH, "r") as f:
        return json.load(f)

def save_onayli_uyeler(data):
    with open(DATA_PATH, "w") as f:
        json.dump(data, f, indent=2)

def onay_goster(update: Update, context: CallbackContext):
    mesaj = """
🎉 *Hoş geldin!*

📜 *Kurallarımız*:
1. Küfür, hakaret, ayrımcılık yasaktır.
2. Dini, milli, ırki tartışmalar yasaktır.
3. Spam, reklam ve link paylaşımı yasaktır.
4. Kavga, huzursuzluk, kargaşa yasaktır.
5. Özel ilişkiler kurulabilir fakat:
   _Burada kurulan ilişkilerden dolayı yaşanacak olaylar grup ya da yöneticileri bağlamaz._

✅ Gruba mesaj atabilmek için /onayla komutunu yazmalısın.
"""
    update.message.reply_text(mesaj, parse_mode="Markdown")

def onayla(update: Update, context: CallbackContext):
    user = update.effective_user
    user_id = user.id
    username = user.username or user.full_name
    onaylilar = load_onayli_uyeler()

    if any(k["id"] == user_id for k in onaylilar):
        update.message.reply_text("Zaten daha önce onay verdiniz 🙂")
        return

    onaylilar.append({
        "id": user_id,
        "username": username,
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    })
    save_onayli_uyeler(onaylilar)
    update.message.reply_text("✅ Teşekkürler! Artık gruba mesaj gönderebilirsiniz.")

def mesaj_kontrol(update: Update, context: CallbackContext):
    user_id = update.effective_user.id
    onaylilar = load_onayli_uyeler()
    if not any(k["id"] == user_id for k in onaylilar):
        try:
            update.message.delete()
        except:
            pass
        context.bot.send_message(chat_id=update.effective_chat.id, text="Mesaj gönderebilmek için önce /onayla yazmalısınız.")

def kayit_ol(dispatcher):
    dispatcher.add_handler(CommandHandler("onay", onay_goster))
    dispatcher.add_handler(CommandHandler("onayla", onayla))
    dispatcher.add_handler(MessageHandler(Filters.text & (~Filters.command), mesaj_kontrol))
