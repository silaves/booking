from django.contrib import admin

from .read_only_admin import ReadOnlyAdminMixin
from applications.service.models import Payment


@admin.register(Payment)
class PaymentAdmin(ReadOnlyAdminMixin, admin.ModelAdmin):
    list_display = ('id', 'payment_amount', 'payment_method', 'sale')
