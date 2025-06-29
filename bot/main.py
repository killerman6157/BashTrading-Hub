bot/main.py

import logging from fastapi import FastAPI, Request, HTTPException from telegram import Bot from telegram.constants import ParseMode from config import BOT_TOKEN, WEBHOOK_SECRET, SIGNAL_CHANNEL_ID import uvicorn

bot = Bot(token=BOT_TOKEN) app = FastAPI()

logging.basicConfig(level=logging.INFO) logger = logging.getLogger(name)

@app.post("/webhook/{secret_key}") async def webhook_handler(secret_key: str, request: Request): if secret_key != WEBHOOK_SECRET: raise HTTPException(status_code=403, detail="Unauthorized webhook")

data = await request.json()
logger.info(f"📥 Received Webhook Data: {data}")

try:
    symbol = data.get("symbol") or data.get("ticker")
    entry = data.get("entry") or data.get("price")
    tp = data.get("tp") or data.get("take_profit")
    sl = data.get("sl") or data.get("stop_loss")
    signal_type = data.get("type") or "Signal"

    message = (
        f"📡 *{signal_type.upper()} Signal*

" f"Pair: {symbol} " f"Entry: {entry} " f"TP: {tp} " f"SL: {sl}" )

await bot.send_message(
        chat_id=SIGNAL_CHANNEL_ID,
        text=message,
        parse_mode=ParseMode.MARKDOWN
    )
    return {"status": "success"}

except Exception as e:
    logger.error(f"❌ Error: {e}")
    raise HTTPException(status_code=500, detail="Server error")

if name == "main": uvicorn.run("bot.main:app", host="0.0.0.0", port=8000, reload=True)

