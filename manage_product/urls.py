from django.urls import path

from .views import index, index_product, order_photo

urlpatterns = [
    path('<uuid:productid>', index_product, name='product'),
    path('orderfoto', order_photo, name='orderfoto'),
    path('', index)
]

