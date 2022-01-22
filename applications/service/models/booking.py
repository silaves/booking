from django.db import models
from django.contrib.auth.models import User

from .base import BaseModel
from .room import Room
from .sale import Sale
from .client import Client

class Booking(BaseModel):
    PENDING = 'pending'
    PAID = 'paid'
    DELETED = 'deleted'

    STATUS = [
        (PENDING, 'Pending'),
        (PAID, 'Paid'),
        (DELETED, 'Deleted')
    ]

    room = models.ForeignKey(Room, related_name='rooms', on_delete=models.CASCADE)
    client = models.ForeignKey(Client, related_name='clients', on_delete=models.CASCADE)
    user = models.ForeignKey(User, related_name='users', on_delete=models.CASCADE)
    sale = models.ForeignKey(Sale, related_name='sales', on_delete=models.CASCADE, null=True)
    date_booking = models.DateTimeField(auto_now_add=True)
    date_entry = models.DateTimeField(null=True)
    date_exit = models.DateTimeField(null=True)
    number_days = models.IntegerField(null=False)
    status = models.CharField(max_length=50, null=False, choices=STATUS)