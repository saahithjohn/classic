from django.contrib import admin
from .models import ResidentProfile

@admin.register(ResidentProfile)
class ResidentProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'flat', 'is_owner', 'is_tenant', 'phone', 'email')
    search_fields = ('user__username', 'flat__number', 'phone', 'email')
    list_filter = ('is_owner', 'is_tenant', 'communication_pref')
