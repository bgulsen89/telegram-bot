from telegram.ext import Updater
from config import TOKEN
from modules import onay_butonu

def main():
    updater = Updater(TOKEN, use_context=True)
    dp = updater.dispatcher

    # Onay sistemini ekle
    onay_butonu.kayit_ol(dp)

    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    main()
