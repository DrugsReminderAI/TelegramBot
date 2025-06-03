from telegram import Update
from telegram.ext import ContextTypes
from .services import send_to_backend

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user
    message = {
        "user_id": user.id,
        "username": user.username,
        "text": update.message.text,
        "timestamp": update.message.date.isoformat()
    }

    #await send_to_backend(message)
    await update.message.reply_text("✅ Принято.")