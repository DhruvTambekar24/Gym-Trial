from fastapi import FastAPI, Request
from fastapi.responses import PlainTextResponse
from app.config import settings
from app.services.twilio_service import TwilioService

app = FastAPI(title=settings.project_name)

@app.get("/health")
async def health():
    return {"status": "ok"}

@app.post("/webhook")
async def webhook(request: Request):
    form = await request.form()
    from_number = form.get("From") or form.get("from")
    body = form.get("Body") or form.get("body")
    TwilioService.send_message(to=from_number or "unknown", body="Thanks! We received your message.")
    return PlainTextResponse("OK")
