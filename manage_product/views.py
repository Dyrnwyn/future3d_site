from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import ProductId

def index(request):
	template = loader.get_template('product.html')
	Products = ProductId.objects.order_by('-template')
	context = {'Products': Products}
	return HttpResponse(template.render(context, request))

