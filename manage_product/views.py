# from django.shortcuts import render
from django.http import HttpResponse, Http404
from django.template import loader
from .models import ProductId, Articles
from menu.models import Menu
from future3d_site.settings import BASE_DIR
from django.http import FileResponse
from ad_message.views import get_active_message
from django.contrib import messages
from .forms import FotoOrderForm
from django.contrib import messages


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
    print(product_uuid.template_name.template_id)
    template = loader.get_template("manage_product/" + str(product_uuid.template_name.template_id) + '.html')
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
    article = Articles.objects.get(id=1)
    section = Menu.objects.order_by('section_number')
    context = {'form': FotoOrderForm, 'article': article.description,
               'section': section}
    template = loader.get_template("manage_product/fotoorder.html")
    if request.method == "POST":
        order_foto = FotoOrderForm(request.POST, request.FILES)
        if order_foto.is_valid():
            order_foto.save()
            messages.add_message(request, messages.INFO, "Запрос успешно отправлен. С Вами скоро свяжутся.")
            return HttpResponse(template.render(context, request))
        else:
            context = {'form': order_foto, 'article': article.description}
            return HttpResponse(template.render(context, request))

    else:
        return HttpResponse(template.render(context, request))
