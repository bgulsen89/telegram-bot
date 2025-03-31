from telegram.ext import Updater
from config import TOKEN
from modules import onay_butonu
from modules import eglence

# Mesaj atılacak grup ID'si (senin grubunun chat_id'si)
CHAT_ID = -1002520321072  # Bunu kendi grubunun ID’siyle değiştirme, doğru zaten :)

def main():
    updater = Updater(TOKEN, use_context=True)
    bot = updater.bot

    # Geri geldim mesajı
    bot.send_message(chat_id=CHAT_ID, text="Hey Beach, Geri geldim burdayım cicişler!")

    # Eğlence sistemi başlat
    eglence.zamanlayici_baslat(bot)

    # Komutları dinleyiciye ekle
    dp = updater.dispatcher
    onay_butonu.kayit_ol(dp)

    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    main()
