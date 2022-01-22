from django.db import models

from .base import BaseModel


class Client(BaseModel):
    nit = models.CharField(max_length=20, null=False, unique=True)
    name = models.CharField(max_length=255, null=False, unique=True)
