# from django.shortcuts import render
from django.http import HttpResponse, Http404
from django.template import loader
from .models import ProductId
from menu.models import Menu
from future3d_site.settings import BASE_DIR
from django.http import FileResponse
from ad_message.views import get_active_message
from django.contrib import messages
from .forms import FotoOrderForm

def index(request):
    template = loader.get_template('product.html')
    Products = ProductId.objects.order_by('-template')
    section = Menu.objects.all()
    context = {'Products': Products, 'section': section}
    return HttpResponse(template.render(context, request))


def index_product(request, productid):
    try:
        product_uuid = ProductId.objects.get(product_id=productid)
    except ProductId.DoesNotExist:
        raise Http404('Такой страницы не существует')
    template = loader.get_template("manage_product/" + product_uuid.template + '.html')
    section = Menu.objects.order_by('section_number')
    if product_uuid.img_jpg.name != '':
        img_jpg = product_uuid.img_jpg.url
    else:
        img_jpg = None
    msg = get_active_message()
    for i in msg:
        messages.add_message(request, messages.INFO, str(i.message))
    context = {'product_img': product_uuid.img.url, 'section': section,
               'img_jpg': img_jpg}
    return HttpResponse(template.render(context, request))


def download_json(request):
    return FileResponse(open(BASE_DIR + '/upload/' + 'product_for_pay.json',
                             'rb'), as_attachment=True,
                        filename='product_for_1c.json')


def order_photo(request):
    pass
