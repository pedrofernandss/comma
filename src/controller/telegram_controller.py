from fastapi import APIRouter, Request
from src.service.channel.telegram import Telegram

telegram_router = APIRouter(prefix="/api/telegram")
_telegram: Telegram | None = None


def get_telegram() -> Telegram:
    global _telegram
    if _telegram is None:
        _telegram = Telegram()
    return _telegram


@telegram_router.post("/webhook")
def webhook(request: Request, update: dict):
    get_telegram().handle_update(update)
    return {"status": "ok"}
