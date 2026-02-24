from sqlalchemy.orm import Session
from src.domain.news import News


def exists_by_url(db: Session, url: str) -> bool:
    return db.query(News).filter(News.url == url).first() is not None


def save(db: Session, news: News) -> News:
    db.add(news)
    db.commit()
    db.refresh(news)
    return news
