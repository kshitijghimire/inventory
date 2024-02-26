from django.shortcuts import render
from .models import Product

# Create your views here.
def productHome(request):
    context = {
        'title':'Products',
        'products':Product.objects.all() #TO get all data from product table
    }
    return render(request,'index.html', context)

def ProductDetail(request):
    return render(request, 'detail.html')
