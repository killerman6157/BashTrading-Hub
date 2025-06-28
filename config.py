# config.py

import os
from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")  # Token daga BotFather
WEBHOOK_SECRET = os.getenv("WEBHOOK_SECRET")  # Secret key daga TradingView webhook
SIGNAL_CHANNEL_ID = os.getenv("SIGNAL_CHANNEL_ID")  # Channel ID ko group ID

# Default fallback idan ba a saka a .env ba
if not BOT_TOKEN:
    raise ValueError("⚠️ BOT_TOKEN bai samu ba. Saka shi a .env file.")
if not WEBHOOK_SECRET:
    raise ValueError("⚠️ WEBHOOK_SECRET bai samu ba. Saka shi a .env file.")
if not SIGNAL_CHANNEL_ID:
    raise ValueError("⚠️ SIGNAL_CHANNEL_ID bai samu ba. Saka shi a .env file.")
