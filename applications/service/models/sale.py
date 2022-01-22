from django.db import models

from .base import BaseModel


class Sale(BaseModel):
    IN_PROGRESS = 'in_progress'
    FINISHED = 'finished'
    CANCELED = 'canceled'

    STATUS = [
        (IN_PROGRESS, 'In progress'),
        (FINISHED, 'Finished'),
        (CANCELED, 'Canceled')
    ]

    INVOICE = 'invoice'
    RECEIPT = 'receipt'

    TYPE_SALE = [
        (INVOICE, 'Invoice'),
        (RECEIPT, 'Receipt')
    ]
    status = models.CharField(max_length=50, null=False, choices=STATUS)
    type_sale = models.CharField(max_length=50, null=False, blank=False, choices=TYPE_SALE)
    total = models.DecimalField(max_digits=7, decimal_places=1, blank=False)
