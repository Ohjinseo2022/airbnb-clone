from django.db import models
from common.models import CommonModel

# Create your models here.
class Photo(CommonModel):
    file = models.ImageField()
    description = models.CharField(
        max_length=140,
    )
    room = models.ForeignKey(
        "rooms.Room",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name="medias",
    )
    experience = models.ForeignKey(
        "experiences.Experiences",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name="medias",
    )

    def __str__(self) -> str:
        return "Photo File"


class Video(CommonModel):
    file = models.FileField()
    experience = models.OneToOneField(
        "experiences.Experiences",
        on_delete=models.CASCADE,
        related_name="videos",
    )

    def __str__(self) -> str:
        return "Video File"
