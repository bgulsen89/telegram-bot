from telegram import Update
from telegram.ext import CallbackContext, MessageHandler, Filters

def yeni_uye_mesaji(update: Update, context: CallbackContext):
    for uye in update.message.new_chat_members:
        update.message.reply_text("Hoş geldin tatlım… 𓆩♡𓆪 Ben Kızıl Bekçi’yim. Sohbeti korurum, sessizliği bozarım.")

def karsilama_ekle(dispatcher):
    dispatcher.add_handler(MessageHandler(Filters.status_update.new_chat_members, yeni_uye_mesaji))