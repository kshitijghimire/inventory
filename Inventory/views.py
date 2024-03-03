from django.shortcuts import render
from .models import Inventory
from .forms import InventoryForm




# Create your views here.
def InventoryHome(request):
    form = InventoryForm()

    context ={
        'forms': form, 
        't':'Inventory management',
        'Inventory':Inventory.objects.all()

    }
    return render(request, 'inventory.html',context)