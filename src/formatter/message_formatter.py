from src.domain.news import News

MAX_DESCRIPTION_LENGTH = 1500


def format_news_to_message(news: News) -> str:
    raw = news.description if news.description else "Check the link for more details!"
    description = (
        raw[:MAX_DESCRIPTION_LENGTH] + "... (read more)"
        if len(raw) > MAX_DESCRIPTION_LENGTH
        else raw
    )
    return (
        "☕ **Time for a Comma ,**\n\n"
        "Life moves fast. Take a break and check this out:\n\n"
        f"📰 **{news.title}**\n\n"
        f"> {description}\n\n"
        f"🔗 [Read full story]({news.url})"
    )
