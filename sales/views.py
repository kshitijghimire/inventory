from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def saleshome(request):
    return render(request,'sales.html')

