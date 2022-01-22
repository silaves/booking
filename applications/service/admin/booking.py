from django.contrib import admin

from .read_only_admin import ReadOnlyAdminMixin
from applications.service.models import Booking


@admin.register(Booking)
class BookingAdmin(ReadOnlyAdminMixin, admin.ModelAdmin):
    list_display = ('id', 'room','client', 'user', 'status', 'number_days', 'date_booking', 'date_entry', 'date_exit',
                    'created_at', 'updated_at')
