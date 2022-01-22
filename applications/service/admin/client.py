from django.contrib import admin

from .read_only_admin import ReadOnlyAdminMixin
from applications.service.models import Client


@admin.register(Client)
class ClientAdmin(ReadOnlyAdminMixin, admin.ModelAdmin):
    list_display = ('id', 'nit', 'name', 'is_active')
