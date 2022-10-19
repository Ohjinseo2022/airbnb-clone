from tabnanny import verbose

from django.db import models

# Create your models here.


class House(models.Model):
    """Model Definition for Houses"""

    name = models.CharField(max_length=140)  # 적당히 길이가 정해진 텍스트
    price_per_night = models.PositiveIntegerField(
        verbose_name="Price", help_text="정수만 가능합니다"
    )  # 정수and 양수 의 값
    description = models.TextField()  # 길이가 정해지지않은 텍스트
    address = models.CharField(max_length=140)  # 주소
    pet_allowed = models.BooleanField(
        verbose_name="Pets Allowed?", default=True, help_text="이 집은 애완동물을 허용하나요?"
    )  # 애완동물 동행가능 유무
    owner = models.ForeignKey("users.User", on_delete=models.CASCADE)

    def __str__(self):
        return self.name
