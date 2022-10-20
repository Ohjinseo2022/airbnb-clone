from django.db import models

# Create your models here.
"""재사용을 위한 모델 설계 데이터베이스에 추가안됨"""


class CommonModel(models.Model):

    """Common Model Defintion"""

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
