from sqlalchemy import Column, BigInteger, String, Boolean

from src.database import Base


class AvailableFeeds(Base):
    __tablename__ = "available_feeds"

    id = Column(BigInteger, primary_key=True, autoincrement=True)
    organization = Column(String(255), nullable=False)
    url = Column(String(850), nullable=False, unique=True)
    is_active = Column(Boolean, nullable=False, default=True)
