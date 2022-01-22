from django.db import models

from .base import BaseModel

class RoomType(BaseModel):
    code = models.CharField(max_length=255, null=False, unique=True)
    description = models.TextField(null=True)
