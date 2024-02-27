from django.shortcuts import render
from .models import Category


# Create your views here.
def CategoryHome(request):
    return render(request,'categories.html')