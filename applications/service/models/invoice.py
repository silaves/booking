from django.db import models

from .base import BaseModel
from .sale import Sale


class Invoice(BaseModel):
    INVOICE = 'invoice'
    RECEIPT = 'receipt'

    TYPE = [
        (INVOICE, 'Invoice'),
        (RECEIPT, 'Receipt')
    ]
    nit = models.CharField(max_length=20, null=False, unique=True)
    client = models.CharField(max_length=255, null=False, unique=True)
    sale = models.ForeignKey(Sale, related_name='invoice_sales', on_delete=models.CASCADE)
    type = models.CharField(max_length=50, null=False, choices=TYPE)
