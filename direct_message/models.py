from django.db import models
from common.models import CommonModel

# Create your models here.


class ChattingRoom(CommonModel):
    """Room Model Definition"""

    users = models.ManyToManyField(
        "users.User",
        related_name="chattingRooms",
    )

    def __str__(self) -> str:
        return f"ChattingRoom"


class Message(CommonModel):
    """Message Model Definition"""

    text = models.TextField()
    user = models.ForeignKey(
        "users.User",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="messages",
    )
    room = models.ForeignKey(
        "direct_message.ChattingRoom",
        on_delete=models.CASCADE,
        related_name="messages",
    )

    def __str__(self) -> str:
        return f"{self.user} says: {self.text}"
