from django.shortcuts import render
from .models import addexpense

# Create your views here.
def expenseHome(request):
    return render(request,'expense.html')
    