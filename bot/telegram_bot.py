import os
import logging
from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv("TELEGRAM_BOT_TOKEN", "YOUR_TOKEN_HERE")

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    referral_link = f"https://t.me/ShockPredictorBot?start={user_id}"
    
    welcome_text = (
        "🤖 **Bienvenido a ShockPredictor PRO**\n\n"
        "Detectamos volatilidad antes que nadie.\n\n"
        "🤝 **Programa de Afiliados:**\n"
        "Comparte tu enlace y gana un 20% de comisión recurrente por cada suscriptor PRO.\n\n"
        f"🔗 Tu link: `{referral_link}`\n\n"
        "Usa /stats para ver tus referidos o /alerts para configurar tus notificaciones."
    )
    await context.bot.send_message(chat_id=update.effective_chat.id, text=welcome_text, parse_mode='Markdown')

async def stats(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # Lógica simulada de estadísticas de afiliados
    stats_text = (
        "📊 **Tus Estadísticas de Afiliado**\n\n"
        "- Clics: 124\n"
        "- Referidos Activos: 8\n"
        "- Comisiones Acumuladas: €46.40\n\n"
        "Pagos automáticos vía PayPal/Crypto al llegar a €50."
    )
    await context.bot.send_message(chat_id=update.effective_chat.id, text=stats_text, parse_mode='Markdown')

async def alert_pro(context: ContextTypes.DEFAULT_TYPE, chat_id, score, reason):
    message = f"⚠️ **ALERTA SHOCK DETECTADA** ⚠️\n\nScore: {score}/100\nCausa: {reason}\n\nAcción recomendada: Revisar exposición en $BTC."
    await context.bot.send_message(chat_id=chat_id, text=message, parse_mode='Markdown')

if __name__ == '__main__':
    application = ApplicationBuilder().token(TOKEN).build()
    
    start_handler = CommandHandler('start', start)
    application.add_handler(start_handler)
    
    print("Bot de Telegram iniciado...")
    # application.run_polling() # Comentado para no bloquear la ejecución en el sandbox
