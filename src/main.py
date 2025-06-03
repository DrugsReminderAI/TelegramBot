import logging
from telegram.ext import ApplicationBuilder, MessageHandler, filters
from .config import BOT_TOKEN
from .handlers import handle_message

logging.basicConfig(level=logging.INFO)

def main():
    app = ApplicationBuilder().token(BOT_TOKEN).build()
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
    app.run_polling()

if __name__ == "__main__":
    main()