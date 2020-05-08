# from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import ProductId
from menu.models import Menu


def index(request):
    template = loader.get_template('product.html')
    Products = ProductId.objects.order_by('-template')
    section = Menu.objects.all()
    context = {'Products': Products, 'section': section}
    return HttpResponse(template.render(context, request))


def index_product(request, productid):
    product_uuid = ProductId.objects.get(product_id=productid)
    template = loader.get_template(product_uuid.template + '.html')
    section = Menu.objects.order_by('section_number')
    context = {'product_img': product_uuid.img.url, 'section': section}
    return HttpResponse(template.render(context, request))
