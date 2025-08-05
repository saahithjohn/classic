from django.contrib import admin
from .models import Flat

@admin.register(Flat)
class FlatAdmin(admin.ModelAdmin):
    list_display = ('number', 'uds_area', 'ownership_type', 'owner', 'tenant', 'is_occupied')
    search_fields = ('number', 'owner__username', 'tenant__username')
    list_filter = ('ownership_type', 'is_occupied')
