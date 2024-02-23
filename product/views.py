from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime

# Create your views here.
def productHome(request):
    context = {
        'title':'Products',
        'today':datetime.now().date(),
        'ch':'I',
        'products':['Laptop','Mouse','Keyboard']
        }
    
    return render(request,'index.html', context)

def ProductDetail(request):
    return render(request, 'detail.html')
