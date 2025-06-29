import logging
from fastapi import FastAPI, Request, HTTPException
import uvicorn

# Import settings daga config.py
from config import BOT_TOKEN, WEBHOOK_SECRET

# Import webhook_entry daga handlers
# KA LURA: webhook_entry yanzu baya buƙatar `update` ko `context`.
# Zai karbi data kai tsaye daga FastAPI webhook.
from handlers.webhook import process_webhook_data # An canza sunan function don karin fayyace

# Saita FastAPI App
app = FastAPI()

# Saita Logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__) # An gyara zuwa __name__

@app.post("/webhook/{secret_key}")
async def webhook_handler(secret_key: str, request: Request):
    """
    Mai karɓar webhook wanda ke kira wani function don sarrafa bayanai.
    """
    # Duba sirrin key
    if secret_key != WEBHOOK_SECRET:
        logger.warning(f"⚠️ Unauthorized webhook attempt with key: {secret_key}")
        raise HTTPException(status_code=403, detail="Unauthorized webhook")

    try:
        data = await request.json()
        logger.info(f"📥 Received Webhook Data in main.py: {data}")

        # Kira function din da ke sarrafa webhook data a handlers/webhook.py
        # Zamu tura masa data da muke samu daga request.
        result = await process_webhook_data(data)
        
        logger.info(f"✅ Webhook data processed by handler: {result.get('message', 'No message')}")
        return {"status": "success", "message": result.get("message", "Data processed.")}

    except Exception as e:
        logger.error(f"❌ Error in main.py webhook handler: {e}", exc_info=True)
        raise HTTPException(status_code=500, detail=f"Server error: {e}")

# Yadda za a tashi da FastAPI app
if __name__ == "__main__":
    logger.info("🚀 Starting FastAPI application...")
    uvicorn.run("bot.main:app", host="0.0.0.0", port=8000, reload=True)

