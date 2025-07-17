from django.contrib import admin
from .models import Court, Slot, ClickLog

admin.site.register(Court)
admin.site.register(Slot)
admin.site.register(ClickLog)