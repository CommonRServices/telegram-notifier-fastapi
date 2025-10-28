from pydantic import BaseModel, Field

from enums import NotificationType


class NotificationReq(BaseModel):
    type: NotificationType = NotificationType.NOTIFICATION
    message: str = Field(
        ..., max_length=2000, description="The message of the Telegram notification"
    )
