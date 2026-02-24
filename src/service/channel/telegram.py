import os
import logging
import requests

from src.domain.news import News
from src.formatter.message_formatter import format_news_to_message

logger = logging.getLogger(__name__)


class Telegram:
    def __init__(self):
        self.token = os.environ["TELEGRAM_BOT_TOKEN"]
        self.base_url = f"https://api.telegram.org/bot{self.token}"
        self.subscribed_chats: set[str] = set()

    def send_message(self, news: News):
        if not self.subscribed_chats:
            logger.warning("No subscribed chats.")
            return
        text = format_news_to_message(news)
        for chat_id in self.subscribed_chats:
            self._send(chat_id, text)

    def handle_update(self, update: dict):
        message = update.get("message", {})
        chat_id = str(message.get("chat", {}).get("id", ""))
        command = message.get("text", "")

        match command:
            case "/subscribe":
                self.subscribed_chats.add(chat_id)
                self._send(chat_id, "✅ Subscribed to Comma news!")
            case "/unsubscribe":
                self.subscribed_chats.discard(chat_id)
                self._send(chat_id, "❌ Unsubscribed from Comma news.")
            case _:
                self._send(chat_id, "Commands: /subscribe, /unsubscribe")

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
