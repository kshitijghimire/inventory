from django.http import HttpResponse
from django.shortcuts import render
from product.models import Product
from Category.models import Category

def home(request):


    products = Product.objects.all().order_by('-id')
    Categories = Category.objects.all().order_by('-id')


    context = {
        'title':'Inventory Management System',
        'products':products,
        'categories':Categories
    }
    return render(request, 'home.html',context)

def sign(request):
    return render(request, 'sign.html')

