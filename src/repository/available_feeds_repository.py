from sqlalchemy.orm import Session
from src.domain.available_feeds import AvailableFeeds


def find_all_active_urls(db: Session) -> list[str]:
    return [f.url for f in db.query(AvailableFeeds).filter(AvailableFeeds.is_active == True).all()]


def find_all(db: Session) -> list[AvailableFeeds]:
    return db.query(AvailableFeeds).all()


def find_by_id(db: Session, feed_id: int) -> AvailableFeeds | None:
    return db.query(AvailableFeeds).filter(AvailableFeeds.id == feed_id).first()


def save(db: Session, feed: AvailableFeeds) -> AvailableFeeds:
    db.add(feed)
    db.commit()
    db.refresh(feed)
    return feed


def delete(db: Session, feed: AvailableFeeds):
    db.delete(feed)
    db.commit()


def exists_by_id(db: Session, feed_id: int) -> bool:
    return db.query(AvailableFeeds).filter(AvailableFeeds.id == feed_id).first() is not None
