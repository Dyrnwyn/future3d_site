from django.urls import path
from django.conf.urls.static import static
from django.conf import settings

from .views import index, index_product

urlpatterns = [
	path('<uuid:productid>', index_product),
	path('', index)
] 

