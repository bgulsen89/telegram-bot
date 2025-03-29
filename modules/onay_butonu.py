from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import CallbackContext, CommandHandler, CallbackQueryHandler
import json
import os
from datetime import datetime

DATA_PATH = "data/onayli_uyeler.json"

def kayit_ol(dispatcher):
    dispatcher.add_handler(CommandHandler("onay", onay_gonder))
    dispatcher.add_handler(CallbackQueryHandler(onayla_buton, pattern="onayla_"))

def onay_gonder(update: Update, context: CallbackContext):
    user = update.effective_user
    chat_id = update.effective_chat.id

    # Butona özel kullanıcı id'sini callback_data içine yaz
    keyboard = [[InlineKeyboardButton("✅ Onaylıyorum", callback_data=f"onayla_{user.id}")]]
    reply_markup = InlineKeyboardMarkup(keyboard)

    context.bot.send_message(
        chat_id=chat_id,
        text="📌 Gruba katılmadan önce aşağıdaki butona basarak kuralları kabul ettiğini onayla.",
        reply_markup=reply_markup
    )

def onayla_buton(update: Update, context: CallbackContext):
    query = update.callback_query
    user = query.from_user
    data = query.data

    try:
        allowed_user_id = int(data.split("_")[1])
    except:
        query.answer("Hatalı veri!", show_alert=True)
        return

    if user.id != allowed_user_id:
        query.answer("Bu buton sana ait değil şekerim 💅", show_alert=True)
        return

    query.answer("Başarıyla onaylandın ✅", show_alert=True)

    os.makedirs("data", exist_ok=True)
    try:
        with open(DATA_PATH, "r", encoding="utf-8") as f:
            kayitlar = json.load(f)
    except:
        kayitlar = []

    if user.id not in [k["id"] for k in kayitlar]:
        kayitlar.append({
            "id": user.id,
            "username": user.username or user.full_name,
            "tarih": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        })
        with open(DATA_PATH, "w", encoding="utf-8") as f:
            json.dump(kayitlar, f, indent=2, ensure_ascii=False)

    # Mesajı düzenle ve butonu kaldır
    context.bot.edit_message_text(
        chat_id=query.message.chat.id,
        message_id=query.message.message_id,
        text="✅ Onay tamamlandı! Artık grupta yazışabilirsin."
    )
