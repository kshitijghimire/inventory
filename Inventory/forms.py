from django import forms
from .models import Inventory

class CategoryForm(forms.ModelForm):

    class Meta:
        model = Inventory
        fields = '__all__' #All Fields