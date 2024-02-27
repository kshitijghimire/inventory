from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def vendorHome(request):
    return render(request, 'vendor.html')