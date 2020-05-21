from django.shortcuts import render
from .models import Faq
from menu.models import Menu
# Create your views here.


def faq(request):
    faq = Faq.objects.all()
    section = Menu.objects.all()
    context = {'faq': faq, 'section': section}
    return render(request, 'faq/faq.html', context=context)
