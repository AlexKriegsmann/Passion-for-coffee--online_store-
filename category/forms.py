from django import forms
from django.forms import TextInput

from category.models import Category


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = '__all__'

        widgets = {
            'name': TextInput(attrs={'class': 'form-control', 'placeholder': 'Please enter category name'})
        }

class CategoryUpdateForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = '__all__'
        widgets = {
            'name': TextInput(attrs={'class': 'form-control', 'placeholder': 'Please enter new category name'})

        }