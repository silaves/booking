from django.contrib import admin

from .read_only_admin import ReadOnlyAdminMixin
from applications.service.models import Room


@admin.register(Room)
class RoomAdmin(ReadOnlyAdminMixin, admin.ModelAdmin):
    list_display = ('id', 'code', 'location', 'description', 'feature', 'status', 'price_by_day', 'is_active',
                    'created_at', 'updated_at')
