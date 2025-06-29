import logging
from telegram import Update
from telegram.ext import ContextTypes
from strategies.smc import analyze_token
from scanner.auto_select import get_best_token

logger = logging.getLogger(__name__)

CHANNEL_ID = -1002603448132  # ⚠️ Canja zuwa Channel ID naka idan ba wannan ba

async def webhook_entry(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Ana kira daga webhook (TradingView), ko kuma a matsayin debugging handler."""
    try:
        # Samu mafi kyau token don analysis
        token = get_best_token()
        if not token:
            await context.bot.send_message(
                chat_id=CHANNEL_ID,
                text="❌ Ba a samo token mai kyau ba a yanzu."
            )
            return

        # Yi analysis da strategy na SMC
        signal = analyze_token(token)
        if not signal:
            await context.bot.send_message(
                chat_id=CHANNEL_ID,
                text=f"❌ Babu signal na gaske don {token['symbol']} yanzu."
            )
            return

        # Aika sakon signal
        message = (
            f"📈 *Real-Time Signal (SMC)*\n"
            f"Token: `{token['symbol']}`\n"
            f"Network: {token['network'].upper()}\n"
            f"Exchange: {token['exchange']}\n"
            f"\n"
            f"🔍 Signal Type: *{signal['type']}*\n"
            f"🧠 Explanation: {signal['description']}\n"
            f"\n"
            f"🕒 Time: {signal['time']}"
        )

        await context.bot.send_message(chat_id=CHANNEL_ID, text=message, parse_mode="Markdown")

    except Exception as e:
        logger.error(f"❌ Kuskure a webhook handler: {e}")
        await context.bot.send_message(
            chat_id=CHANNEL_ID,
            text="❌ An samu kuskure yayin aika signal."
        )
