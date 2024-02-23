from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def InventoryHome(request):

    return HttpResponse('I am going to support Inventory')