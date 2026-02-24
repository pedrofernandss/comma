from src.controller.telegram_controller import telegram_router
from src.controller.available_feeds_controller import feeds_router
from src.controller.news_controller import news_router
from fastapi import FastAPI
import uvicorn
import logging
from dotenv import load_dotenv
load_dotenv()


logging.basicConfig(level=logging.INFO,
                    format="%(asctime)s %(levelname)s %(name)s: %(message)s")

app = FastAPI(title="Comma")
app.include_router(news_router)
app.include_router(feeds_router)
app.include_router(telegram_router)

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8080, reload=False)
