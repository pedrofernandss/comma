import logging
import random
from sqlalchemy.orm import Session
from src.fetcher.rss_fetcher import fetch_news
from src.service.llm.groq_llm import GroqLLM
import src.repository.news_repository as news_repo
import src.repository.available_feeds_repository as feeds_repo

logger = logging.getLogger(__name__)

_llm = GroqLLM()


def choose_news(db: Session, chat_id: str = None):
    try:
        active_urls = feeds_repo.find_all_active_urls(db)
        if not active_urls:
            logger.warning("No active feed URLs found.")
            return None

        url = random.choice(active_urls)
        news_list = fetch_news(url)

        for news in news_list:
            if not news_repo.exists_by_url(db, news.url):
                news.description = _llm.summarize_news(news.description)
                news_repo.save(db, news)

                if chat_id:
                    from src.service.channel.telegram import Telegram

                    Telegram().send_message(news, chat_id)

                return news

        logger.info("No new articles found in this source.")
    except Exception as e:
        logger.error(f"Failed to choose news: {e}")
    return None
