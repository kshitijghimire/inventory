from django.contrib import admin
from .models import sales

class salesAdmin(admin.ModelAdmin):
    list_display = ('product_id','quantity','rate','total','discount','grandTotal','date')

# Register your models here.
admin.site.register(sales, salesAdmin)

