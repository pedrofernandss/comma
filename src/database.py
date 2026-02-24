import os
from dotenv import load_dotenv
from sqlalchemy import create_engine, URL
from sqlalchemy.orm import declarative_base, sessionmaker

load_dotenv()

Base = declarative_base()

engine = create_engine(
    URL.create(
        drivername="mssql+pymssql",
        username=os.environ["DB_USERNAME"],
        password=os.environ["DB_PASSWORD"],
        host="comma-bot.database.windows.net",
        database="comma-database",
    )
)

SessionLocal = sessionmaker(bind=engine, autocommit=False, autoflush=False)


def get_session():
    session = SessionLocal()
    try:
        yield session
    finally:
        session.close()
