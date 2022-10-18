from unittest.util import _MAX_LENGTH
from django.db import models

# Create your models here.
"""Model Definition for Houses"""

class House(models.Model):
  name = models.CharField(max_length=140) #적당히 길이가 정해진 텍스트
  price = models.PositiveIntegerField() # 정수and 양수 의 값
  description = models.TextField() #길이가 정해지지않은 텍스트
  address = models.CharField(max_length=140)  #주소