from django.contrib import admin

from .models import Reservation


@admin.register(Reservation)
class ReservationAdmin(admin.ModelAdmin):
    list_display = ("name", "preferred_date", "arrival_time", "party_size", "status", "created_at")
    list_filter = ("status", "preferred_date", "seating_preference")
    search_fields = ("name", "contact", "notes")
    ordering = ("-created_at",)
