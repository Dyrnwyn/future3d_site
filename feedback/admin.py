from django.contrib import admin
from .models import Feedback


class FeedbackAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'subject')
    list_display_links = ('name',)


admin.site.register(Feedback, FeedbackAdmin)
