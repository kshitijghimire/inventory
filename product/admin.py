from django.contrib import admin
from .models import Product


class ProductAdmin(admin.ModelAdmin):
    list_display = ('name','sku', 'quantity', 'price', 'thumbnail')
    search_fields = ['name']

# Register your models here.
admin.site.register(Product, ProductAdmin)


