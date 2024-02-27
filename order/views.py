from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def orderHome(request):
    return render(request, 'order.html')