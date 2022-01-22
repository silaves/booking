from django.contrib import admin

from .read_only_admin import ReadOnlyAdminMixin
from applications.service.models import RoomType


@admin.register(RoomType)
class RoomTypeAdmin(ReadOnlyAdminMixin, admin.ModelAdmin):
    list_display = ('id', 'code', 'description', 'created_at', 'updated_at')
