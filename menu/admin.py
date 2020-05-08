from django.contrib import admin
from .models import Menu


class MenuAdmin(admin.ModelAdmin):
    list_display = ('section_number', 'section_name', 'section_url')


admin.site.register(Menu, MenuAdmin)
