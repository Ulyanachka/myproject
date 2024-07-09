from django import forms
from .models import Product

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['photo',]  # Список полей, которые вы хотите включить в форму
