from telegram.ext import MessageHandler, Filters
import re

def reklam_kontrol(update, context):
    mesaj = update.message.text
    if re.search(r"(t\.me|telegram\.me|@[\w]+)", mesaj):
        update.message.delete()
        update.message.reply_text("Bu grupta reklam yasak! Lütfen kurallara uy.")
        # Buraya susturma sistemi eklenebilir

def reklam_filtresi_ekle(dispatcher):
    dispatcher.add_handler(MessageHandler(Filters.text & Filters.group, reklam_kontrol))