from django.contrib import admin
from .models import ProductId

class ProductIdAdmin(admin.ModelAdmin):
	list_display = ('product_id', 'template', 'payment_id', 'paid')
	list_display_links = ('product_id', 'template')


admin.site.register(ProductId, ProductIdAdmin)

# Register your models here.
