from django.contrib import admin
from .models import Product, Cart, CartItem
from django.utils.html import format_html, urlencode
from . import models

# Register your models here.
admin.site.register(Cart)
admin.site.register(CartItem)


class ProductImageInline(admin.TabularInline):
    model = models.ProductImage
    readonly_fields = ['thumbnail']

    def thumbnail(self, instance):
        if instance.image.name != '':
            return format_html(f'<img src="{instance.image.url}" class="thumbnail">')
        return ''

    class Media:
        css = {
            'all': ['shop/styles.css']
        }


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    inlines = [ProductImageInline]
    list_display = ['title', 'unit_price']
    list_editable = ['unit_price']
    list_per_page = 10
    search_fields = ['title']


class OrderItemInline(admin.TabularInline):
    autocomplete_fields = ['product']
    min_num = 1
    max_num = 10
    model = models.OrderItem
    extra = 0


@admin.register(models.Order)
class OrderAdmin(admin.ModelAdmin):
    inlines = [OrderItemInline]
    list_display = ['id', 'placed_at',]
