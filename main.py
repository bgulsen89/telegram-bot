from telegram.ext import Updater
from config import TOKEN
from modules import onay_sistemi
from modules.karsilama import karsilama_ekle
from modules.reklam_filtresi import reklam_filtresi_ekle
from modules.test_komutlari import test_komutlarini_ekle

def main():
    updater = Updater(TOKEN, use_context=True)
    dp = updater.dispatcher

    # Modülleri ekle
    karsilama_ekle(dp)
    reklam_filtresi_ekle(dp)
    test_komutlarini_ekle(dp)
    onay_sistemi.kayit_ol(dp)

    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    main()
