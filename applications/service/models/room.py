from django.db import models

from .base import BaseModel
from .room_type import RoomType

class Room(BaseModel):
    AVAILABLE = 'available'
    BOOKED = 'booked'
    MAINTENANCE = 'maintenance'

    STATUS = [
        (AVAILABLE, 'Available'),
        (BOOKED, 'Booked'),
        (MAINTENANCE, 'Maintenance')
    ]

    code = models.CharField(max_length=255, null=False, unique=True)
    location = models.CharField(max_length=255, null=False)
    description = models.TextField(null=True)
    feature = models.TextField(null=True)
    price_by_day = models.DecimalField(max_digits=7, decimal_places=1, blank=False)
    status = models.CharField(max_length=50, null=False, choices=STATUS)
    room_type = models.ForeignKey(RoomType, related_name='room_types', on_delete=models.CASCADE)
