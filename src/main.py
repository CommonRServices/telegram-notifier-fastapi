from fastapi import FastAPI, status
from fastapi.middleware.cors import CORSMiddleware

from logger import logger
from schemas import NotificationReq
from enums import NotificationType
from bot import telegram_bot
from messages import send_message, format_error_message, format_notification_message
from config import CHAT_ID


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/health-check")
async def health_checking():
    return "Service healthy."


@app.post("/", status_code=status.HTTP_201_CREATED)
async def send_notification(data: NotificationReq):
    logger.info("Received notification call.")
    if NotificationType.NOTIFICATION:
        await send_message(
            telegram_bot, CHAT_ID, format_notification_message(data.message)
        )
    else:
        await send_message(telegram_bot, CHAT_ID, format_error_message(data.message))
    logger.info("Notification send.")

    return "OK"
