from django.db import models

from .base import BaseModel
from .payment_method import PaymentMethod
from .sale import Sale


class Payment(BaseModel):
    payment_amount = models.DecimalField(max_digits=7, decimal_places=1, blank=False)
    payment_method = models.ForeignKey(PaymentMethod, related_name='payment_methods', on_delete=models.CASCADE)
    sale = models.ForeignKey(Sale, related_name='payment_sales', on_delete=models.CASCADE)
