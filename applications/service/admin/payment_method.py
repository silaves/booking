from django.contrib import admin

from .read_only_admin import ReadOnlyAdminMixin
from applications.service.models import PaymentMethod


@admin.register(PaymentMethod)
class PaymentMethodAdmin(ReadOnlyAdminMixin, admin.ModelAdmin):
    list_display = ('id', 'number_document', 'type_method')
