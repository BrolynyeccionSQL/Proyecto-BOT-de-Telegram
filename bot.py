from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes
from config import BOT_TOKEN

# Comando /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("¡Hola! Soy un bot que repite todo lo que dices. 😊")

# Echo de mensajes
async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(update.message.text)

# Configuración principal del bot
def main():
    app = ApplicationBuilder().token(BOT_TOKEN).build()

    # Añadir manejadores
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo))

    # Iniciar el bot
    print("Bot iniciado...")
    app.run_polling()

if __name__ == "__main__":
    main()
