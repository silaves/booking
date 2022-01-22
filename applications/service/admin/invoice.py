from django.contrib import admin

from .read_only_admin import ReadOnlyAdminMixin
from applications.service.models import Invoice


@admin.register(Invoice)
class InvoiceAdmin(ReadOnlyAdminMixin, admin.ModelAdmin):
    list_display = ('id', 'nit', 'client', 'sale', 'type')
