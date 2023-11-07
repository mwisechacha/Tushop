from shop.models import Product
from django.contrib import admin
from django.contrib.contenttypes.admin import GenericTabularInline
from shop.admin import ProductAdmin, ProductImageInline

# Register your models here.



class CustomProductAdmin(ProductAdmin):
    inlines = [ProductImageInline]


admin.site.unregister(Product)
admin.site.register(Product, CustomProductAdmin)