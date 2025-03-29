from telegram.ext import CommandHandler

def test(update, context):
    update.message.reply_text("Bot sorunsuz çalışıyor!")

def test_komutlarini_ekle(dispatcher):
    dispatcher.add_handler(CommandHandler("test", test))