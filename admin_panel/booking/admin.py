from django.contrib import admin
from .models import Court, Slot

@admin.register(Court)
class CourtAdmin(admin.ModelAdmin):
    list_display = ("name", "city", "adaptive_support", "booking_url")
    search_fields = ("name", "city")

@admin.register(Slot)
class SlotAdmin(admin.ModelAdmin):
    list_display = ("court", "date", "time", "is_available")
    list_filter = ("court", "is_available", "date")
