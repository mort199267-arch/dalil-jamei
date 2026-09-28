import logging
from telegram.ext import ApplicationBuilder, CommandHandler, CallbackQueryHandler
from config import BOT_TOKEN
from database import init_db
from handlers import start_command, handle_callback

logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO
)
logger = logging.getLogger(__name__)

def main():
    init_db()
    print(" [1/3] تم تهيئة قاعدة البيانات بنجاح.")

    if not BOT_TOKEN or "ضع_التوكن" in BOT_TOKEN:
        print("خطأ: يرجى التأكد من التوكن داخل config.py!")
        return

    application = ApplicationBuilder().token(BOT_TOKEN).build()
    print(" [2/3] تم الاتصال بخوادم تيليجرام بنجاح.")

    application.add_handler(CommandHandler("start", start_command))
    application.add_handler(CallbackQueryHandler(handle_callback))

    print(" [3/3] 🎓 بوت دليل جامعي يعمل الآن بنجاح! جربه من تيليجرام.")
    print("--------------------------------------------------")

    application.run_polling(drop_pending_updates=True)

if __name__ == "__main__":
    main()
