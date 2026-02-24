from fastapi import APIRouter, Depends, HTTPException
from pydantic import BaseModel
from sqlalchemy.orm import Session

from src.database import get_session
from src.domain.available_feeds import AvailableFeeds
import src.repository.available_feeds_repository as feeds_repo

feeds_router = APIRouter(prefix="/api/feeds")


class FeedRequest(BaseModel):
    organization: str
    url: str
    is_active: bool = True


class FeedResponse(BaseModel):
    id: int
    organization: str
    url: str
    is_active: bool

    model_config = {"from_attributes": True}


@feeds_router.post("/", status_code=201, response_model=FeedResponse)
def create(body: FeedRequest, db: Session = Depends(get_session)):
    feed = AvailableFeeds(organization=body.organization,
                          url=body.url, is_active=body.is_active)
    return feeds_repo.save(db, feed)


@feeds_router.get("/", response_model=list[FeedResponse])
def find_all(db: Session = Depends(get_session)):
    return feeds_repo.find_all(db)


@feeds_router.get("/active-urls", response_model=list[str])
def find_all_active_urls(db: Session = Depends(get_session)):
    return feeds_repo.find_all_active_urls(db)


@feeds_router.patch("/{feed_id}", response_model=FeedResponse)
def update_partial(feed_id: int, body: FeedRequest, db: Session = Depends(get_session)):
    feed = feeds_repo.find_by_id(db, feed_id)
    if not feed:
        raise HTTPException(status_code=404, detail="Not found")
    feed.organization = body.organization
    feed.url = body.url
    feed.is_active = body.is_active
    return feeds_repo.save(db, feed)


@feeds_router.delete("/{feed_id}", status_code=204)
def delete(feed_id: int, db: Session = Depends(get_session)):
    feed = feeds_repo.find_by_id(db, feed_id)
    if not feed:
        raise HTTPException(status_code=404, detail="Not found")
    feeds_repo.delete(db, feed)
