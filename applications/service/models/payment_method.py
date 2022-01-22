from django.db import models

from .base import BaseModel
from .room_type import RoomType


class PaymentMethod(BaseModel):
    number_document = models.CharField(max_length=255, null=True)
    type_method = models.CharField(max_length=255, null=False)
