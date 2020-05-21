from django.urls import path

from .views import index, index_product

urlpatterns = [
	path('<uuid:productid>', index_product),
	path('', index)
] 

