import logging
import feedparser
from datetime import datetime

from src.domain.news import News

logger = logging.getLogger(__name__)


def fetch_news(url: str) -> list[News]:
    news_list = []
    try:
        feed = feedparser.parse(url)
        for entry in feed.entries:
            published_at = None
            if getattr(entry, "published_parsed", None):
                published_at = datetime(*entry.published_parsed[:6])

            description = _extract_description(entry)

            news_list.append(
                News(
                    title=entry.get("title", ""),
                    url=entry.get("link", ""),
                    description=description,
                    published_at=published_at,
                    processed_at=datetime.now(),
                )
            )
    except Exception as e:
        logger.error(f"Failed to fetch RSS from {url}: {e}")
    return news_list


def _extract_description(entry) -> str:
    if getattr(entry, "content", None):
        value = entry.content[0].get("value", "")
        if value:
            return value
    if getattr(entry, "summary", None):
        return entry.summary
    logger.warning(f"No content found for: {entry.get('title', '')}")
    return "No content available"
