from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    context = {
        'title':'Inventory Management System'
    }
    return render(request, 'home.html',context)

def main(request):
    return render(request, 'main.html')
