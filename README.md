📱 Yadda Ake Deploy Bot Din a Termux

Bot ɗin BashTrading-Hub yana iya aiki kai tsaye a cikin Termux, wanda ke ba da damar gudanar da Telegram bot ɗin smart money strategy daga waya ba tare da VPS ko PC ba.

✅ Abubuwan da ake bukata

Python 3

pip

git

(zabi) ngrok idan zaka yi amfani da webhook



---

🛠️ Matakan Shigarwa

1. Sabunta Termux da shigar da Python da Git

pkg update && pkg upgrade
pkg install python git
pip install --upgrade pip

2. Clone GitHub repo

git clone https://github.com/killerman6157/BashTrading-Hub.git
cd BashTrading-Hub

3. Install dependencies

pip install -r requirements.txt

4. Kirkiri .env file

cp .env.example .env

Sannan ka gyara .env ka saka bayanan ka:

BOT_TOKEN=your_telegram_bot_token
TRADINGVIEW_WEBHOOK_SECRET=secure_password
ADMIN_ID=6281246656

5. Run the bot

python main.py


---

🌐 (ZABI) Idan Kana son Webhook ta TradingView

6. Install ngrok

pkg install wget unzip
wget https://bin.equinox.io/c/bNyj1mQVY4c/ngrok-stable-linux-arm.zip
unzip ngrok-stable-linux-arm.zip
./ngrok authtoken YOUR_NGROK_AUTH_TOKEN

7. Run ngrok

./ngrok http 8000

8. Set Webhook a TradingView

Je zuwa TradingView alerts

Webhook URL ɗinka zai kasance kamar haka:


https://xxxxx.ngrok.io/webhook/your-secret


---

🔁 Zaka Iya Sake Gudanar da Bot:

cd BashTrading-Hub
python main.py
