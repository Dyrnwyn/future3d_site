from django.shortcuts import render
from .models import AdMessage


def get_active_message():
    msg = AdMessage.objects.filter(is_active=True)
    return msg
