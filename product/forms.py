from django import forms
from django.forms import TextInput, Textarea, Select, NumberInput

from product.models import Product


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'

        widgets = {
            'title': TextInput(attrs={'class': 'form-control', 'placeholder': 'Please enter product name'}),
            'description': Textarea(attrs={'class': 'form-control', 'placeholder': 'Enter description here',
                                           'rows': 5}),
            'category': Select(attrs={'class': 'form-select'}),
            'price': NumberInput(attrs={'class': 'form-control'})
            }

class ProductUpdateForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'

        widgets = {
            'title': TextInput(attrs={'class': 'form-control', 'placeholder': 'Please enter product name'}),
            'description': Textarea(attrs={'class': 'form-control', 'placeholder': 'Enter description here',
                                           'rows': 5}),
            'category': Select(attrs={'class': 'form-select'}),
            'price': NumberInput(attrs={'class': 'form-control'})
        }