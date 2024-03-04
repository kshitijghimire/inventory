from django import forms
from .models import customer

class customerForm(forms.ModelForm):

    class meta:
        
        model = customer
        fields = '__all__'