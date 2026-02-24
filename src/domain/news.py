from sqlalchemy import Column, BigInteger, String, DateTime
from src.database import Base
from datetime import datetime


class News(Base):
    __tablename__ = "news"

    id = Column(BigInteger, primary_key=True, autoincrement=True)
    title = Column(String(500), nullable=False)
    url = Column(String(850), nullable=False, unique=True)
    description = Column(String, nullable=False)
    published_at = Column(DateTime, nullable=True)
    processed_at = Column(DateTime, nullable=True, default=datetime.now)
