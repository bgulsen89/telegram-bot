from telegram.ext import Updater
from config import TOKEN
from modules import onay_butonu
from modules import eglence

def main():
    eglence.zamanlayici_baslat(updater.bot)
    updater = Updater(TOKEN, use_context=True)
    dp = updater.dispatcher

    # Onay sistemini ekle
    onay_butonu.kayit_ol(dp)

    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    main()
