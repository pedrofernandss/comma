import logging
import os
import requests
from src.domain.news import News
from src.formatter.message_formatter import format_news_to_message

logger = logging.getLogger(__name__)


class Discord:
    def __init__(self):
        self.webhook_url = os.environ["DISCORD_TOKEN"]

    def send_message(self, news: News):
        try:
            message = format_news_to_message(news)
            response = requests.post(
                self.webhook_url, json={"content": message})
            if response.status_code == 204:
                logger.info(f"News sent to Discord: {news.title}")
            else:
                logger.error(
                    f"Discord error ({response.status_code}): {response.text}")
        except Exception as e:
            logger.error(f"Failed to send Discord message: {e}")
