import uvicorn
from fastapi import FastAPI
from dotenv import load_dotenv

load_dotenv()

from src.controller.telegram_controller import telegram_router
from src.controller.available_feeds_controller import feeds_router
from src.controller.news_controller import news_router


app = FastAPI(title="Comma")

app.include_router(news_router)
app.include_router(feeds_router)
app.include_router(telegram_router)

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8080, reload=False)
