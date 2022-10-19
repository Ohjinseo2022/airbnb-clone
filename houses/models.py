from unittest.util import _MAX_LENGTH
from django.db import models

# Create your models here.


class House(models.Model):
  """Model Definition for Houses"""
  name = models.CharField(max_length=140) #적당히 길이가 정해진 텍스트
  price_per_night = models.PositiveIntegerField() # 정수and 양수 의 값
  description = models.TextField() #길이가 정해지지않은 텍스트
  address = models.CharField(max_length=140)  #주소
  pet_allowed = models.BooleanField(default=True) # 애완동물 동행가능 유무 