from telegram import Bot


async def send_message(telegram_bot: Bot, chat_id: str, message: str):
    await telegram_bot.send_message(chat_id=chat_id, text=message, parse_mode="HTML")


def format_error_message(message: str) -> str:
    return f"""
    Error notification:
    {message}
    """


def format_notification_message(message: str) -> str:
    return f"""
    Notification:
    {message}
    """
