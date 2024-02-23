from django.contrib import admin
from .models import Product


class ProductAdmin(admin.ModelAdmin):
    list_display = ('name','sku','category', 'quantity', 'price', 'thumbnail')

# Register your models here.
admin.site.register(Product, ProductAdmin)
