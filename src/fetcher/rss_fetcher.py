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
            if hasattr(entry, "published_parsed") and entry.published_parsed:
                published_at = datetime(*entry.published_parsed[:6])

            news = News(
                title=entry.get("title", ""),
                url=entry.get("link", ""),
                description=_extract_description(entry),
                published_at=published_at,
                processed_at=datetime.now(),
            )
            news_list.append(news)
    except Exception as e:
        logger.error(f"Failed to fetch RSS from {url}: {e}")
    return news_list


def _extract_description(entry) -> str:
    if hasattr(entry, "content") and entry.content:
        return entry.content[0].get("value", "")
    if hasattr(entry, "summary"):
        return entry.summary
    logger.warning(f"No content found for entry: {entry.get('title', '')}")
    return "No content available"
