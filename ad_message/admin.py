from django.contrib import admin
from .models import AdMessage


class AdMessageAdmin(admin.ModelAdmin):
    list_display = ('is_active', 'message')


admin.site.register(AdMessage, AdMessageAdmin)
