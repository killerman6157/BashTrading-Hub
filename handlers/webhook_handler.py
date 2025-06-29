import logging
from telegram import Bot
from telegram.constants import ParseMode # Don amfani da Markdown a cikin sako

# Import settings daga config.py
from config import BOT_TOKEN, SIGNAL_CHANNEL_ID # Muna bukatar bot token anan

# Import functions daga scanner da strategies
from strategies.smc import analyze_token
from scanner.auto_select import get_best_token

logger = logging.getLogger(__name__) # An gyara zuwa __name__

# Saita Telegram Bot a nan ma, saboda wannan module din yana amfani da shi
bot = Bot(token=BOT_TOKEN)

# An canza sunan function daga webhook_entry zuwa process_webhook_data
# Kuma an canza sigar sa don ya karbi 'data' kai tsaye daga FastAPI webhook.
async def process_webhook_data(data: dict):
    """
    Wannan function yana sarrafa data da aka karba daga FastAPI webhook,
    yana yin analysis na SMC, sannan yana aikawa sakon signal zuwa Telegram.
    """
    logger.info(f"⚙️ Processing webhook data in handler: {data}")
    try:
        # Zaka iya amfani da data din webhook anan
        symbol_from_webhook = data.get("symbol") or data.get("ticker", "N/A")
        signal_type_from_webhook = data.get("type", "Signal").upper()

        # Samu mafi kyau token don analysis (idan kana so ka yi amfani da scanner)
        token_info = get_best_token()
        if not token_info:
            await bot.send_message(
                chat_id=SIGNAL_CHANNEL_ID,
                text=f"❌ Ba a samo token mai kyau ba a yanzu (daga webhook handler). Tushen: {symbol_from_webhook}"
            )
            logger.warning("No best token found by scanner.")
            return {"status": "failed", "message": "No suitable token found."}

        # Yi analysis da strategy na SMC
        # KA LURA: `analyze_token` yana buƙatar OHLC data.
        # Wannan misali ne kawai. Kana buƙatar aiwatar da yadda zaka samu
        # real-time OHLC data (misali, ta hanyar kiran API na musayar kasuwanci).
        # A yanzu, zan yi amfani da sample data ko kuma ka samar da hanyar.
        
        # Misali na samun OHLC data (kana buƙatar aiwatar da shi)
        # ohlc_data = await fetch_ohlc_data_from_exchange(token_info['symbol'], '1h')
        # if not ohlc_data:
        #    logger.error(f"❌ Failed to fetch OHLC data for {token_info['symbol']}")
        #    return {"status": "failed", "message": f"Failed to fetch OHLC data for {token_info['symbol']}"}
        
        # KIRA analyze_token da real OHLC data
        # signal_result = analyze_token(ohlc_data) # Kuna buƙatar samar da wannan data
        
        # Domin gwaji, bari mu yi amfani da signal daga webhook kai tsaye
        # ko kuma wani misali idan ba za mu iya samun OHLC data ba tukuna.
        
        # Idan kana so ka yi amfani da SMC, zai yi kama da haka:
        # signal_result = analyze_token(some_real_ohlc_data)
        # if not signal_result or not signal_result['signal']:
        #     await bot.send_message(
        #         chat_id=SIGNAL_CHANNEL_ID,
        #         text=f"❌ Babu signal na gaske don {token_info['symbol']} yanzu (daga SMC)."
        #     )
        #     logger.info(f"No strong SMC signal for {token_info['symbol']}.")
        #     return {"status": "no_signal", "message": "No strong SMC signal."}

        # Idan ka karbi signal kai tsaye daga TradingView, zaka iya amfani da bayanan kamar haka:
        message = (
            f"📈 *Real-Time Signal (SMC via Webhook)*\n"
            f"Token: `{symbol_from_webhook}`\n" # Zaka iya amfani da token_info['symbol'] idan scanner ya yi aiki
            f"Source Type: {signal_type_from_webhook}\n"
            f"\n"
            f"🔍 Entry: {data.get('entry', 'N/A')}\n"
            f"🎯 TP: {data.get('tp', 'N/A')}\n"
            f"🛑 SL: {data.get('sl', 'N/A')}\n"
            f"\n"
            f"🕒 Lokaci: {data.get('time', 'Unknown')}" # Idan webhook ya turo lokaci
        )
        
        # Idan kuma kana so ka nuna sakamakon SMC analysis din da ka samu a sama
        # message += f"\n\n🧠 SMC Explanation: {signal_result.get('note', 'N/A')}"

        await bot.send_message(chat_id=SIGNAL_CHANNEL_ID, text=message, parse_mode=ParseMode.MARKDOWN)
        logger.info("✅ Signal sent to Telegram from handler.")
        return {"status": "success", "message": "Signal sent from handler."}

    except Exception as e:
        logger.error(f"❌ Kuskure a webhook handler (process_webhook_data): {e}", exc_info=True)
        await bot.send_message(
            chat_id=SIGNAL_CHANNEL_ID,
            text=f"❌ An samu kuskure yayin aikawa signal (daga handler): {e}"
        )
        return {"status": "error", "message": f"Error in handler: {e}"}

