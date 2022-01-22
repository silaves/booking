from django.db import models


class BaseModel(models.Model):
    created_at = models.DateTimeField(null=False, auto_now_add=True)
    updated_at = models.DateTimeField(null=False, auto_now=True)
    is_active = models.BooleanField(default=True, blank=True)

    class Meta:
        abstract = True
