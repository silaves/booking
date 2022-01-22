from django.contrib import admin

from .read_only_admin import ReadOnlyAdminMixin
from applications.service.models import Sale


@admin.register(Sale)
class SaleAdmin(ReadOnlyAdminMixin, admin.ModelAdmin):
    list_display = ('id', 'status', 'type_sale', 'total')
