📱 BashTrading-Hub Smart Money Entry Bot

BashTrading-Hub bot yana karɓar sakonni daga TradingView webhook sannan yana duba ko signal ɗin ya cika sharuddan Smart Money Concept (SMC). Idan ya dace, bot ɗin zai tura signal kai tsaye zuwa Telegram Channel/Group.


---

🔧 Abubuwan da Bot ɗin ke Kunsha

✅ Webhook Handler – Yana karɓar signal daga TradingView.

✅ SMC Strategy Filter – Duba BOS, FVG, OB da sauran sharudda kafin aika signal.

✅ Auto Scanner – Zabi token ko coin mafi kyau da ya fi cancanta da yanayin kasuwa.

✅ Telegram Integration – Tura sakonni zuwa Channel ko Group.

✅ Modular Structure – handlers/, strategies/, scanner/, config.py, main.py



---

🛠️ Installation & Setup

1. Clone Repo

git clone https://github.com/killerman6157/BashTrading-Hub.git
cd BashTrading-Hub

2. Install Requirements

pip install -r requirements.txt

3. Create .env File

nano .env

Sai ka saka:

BOT_TOKEN=YOUR_TELEGRAM_BOT_TOKEN
WEBHOOK_SECRET=YOUR_SECRET_KEY
TELEGRAM_CHAT_ID=YOUR_CHANNEL_OR_GROUP_ID

> 💡 BOT_TOKEN daga @BotFather
💡 TELEGRAM_CHAT_ID = -100xxxxxxxxxx for channels/groups
💡 WEBHOOK_SECRET ana amfani da shi don tabbatar da webhook ɗin da TradingView ke aiko wa.




---

🧪 How to Test Locally

python main.py

Zaka iya amfani da Ngrok ko LocalTunnel don buɗe webhook ɗinka:

ngrok http 8000

Sai ka sa webhook URL ɗinka a TradingView kamar haka:

https://YOUR_NGROK_URL/webhook?secret=YOUR_SECRET_KEY


---

📤 Format na Webhook Message daga TradingView

{
  "symbol": "BTCUSDT",
  "price": 28500,
  "direction": "BUY",
  "bos": true,
  "ob": true,
  "fvg": true,
  "timeframe": "15m"
}


---

📎 Abubuwan Da Bot Din Ke Aiki Da Su

strategies/smc.py – Smart Money Concept logic

scanner/auto_select.py – Zabi token/coin mafi kyau

handlers/webhook_handler.py – Karɓar sakonni daga webhook

bot/main.py – Entry point na bot

config.py – Cikakken settings da environment variables



---

📦 requirements.txt

python-telegram-bot==20.8
aiohttp==3.9.5
requests==2.31.0
python-dotenv==1.0.1
