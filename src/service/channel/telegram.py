import os
import logging
import requests
from sqlalchemy.orm import Session

from src.domain.news import News
from src.formatter.message_formatter import format_news_to_message

logger = logging.getLogger(__name__)


class Telegram:
    def __init__(self):
        self.token = os.environ["TELEGRAM_BOT_TOKEN"]
        self.base_url = f"https://api.telegram.org/bot{self.token}"

    def send_message(self, news: News, chat_id: str):
        self._send(chat_id, format_news_to_message(news))

    def handle_update(self, update: dict, db: Session):
        message = update.get("message", {})
        chat_id = str(message.get("chat", {}).get("id", ""))
        command = message.get("text", "")

        match command:
            case "/news":
                from src.service.news_service import choose_news
                news = choose_news(db, chat_id)
                if not news:
                    self._send(chat_id, "No new articles found.")
            case _:
                self._send(chat_id, "Commands: /news")

    def _send(self, chat_id: str, text: str):
        try:
            response = requests.post(
                f"{self.base_url}/sendMessage",
                json={"chat_id": chat_id, "text": text,
                      "parse_mode": "Markdown"},
            )
            if not response.ok:
                logger.error(
                    f"Telegram error ({response.status_code}): {response.text}")
        except Exception as e:
            logger.error(f"Failed to send Telegram message: {e}")
