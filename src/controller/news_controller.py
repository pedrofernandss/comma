from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from src.database import get_session
from src.service.news_service import choose_news

news_router = APIRouter(prefix="/api/news")


@news_router.post("/trigger")
def trigger(db: Session = Depends(get_session)):
    news = choose_news(db)
    if news:
        return {"title": news.title, "url": news.url, "description": news.description}
    return {"message": "No new articles found."}
