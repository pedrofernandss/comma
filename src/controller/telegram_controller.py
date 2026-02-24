from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from src.database import get_session
from src.service.channel.telegram import Telegram

telegram_router = APIRouter(prefix="/api/telegram")
_telegram: Telegram | None = None


def get_telegram() -> Telegram:
    global _telegram
    if _telegram is None:
        _telegram = Telegram()
    return _telegram


@telegram_router.post("/webhook")
def webhook(update: dict, db: Session = Depends(get_session)):
    get_telegram().handle_update(update, db)
    return {"status": "ok"}
