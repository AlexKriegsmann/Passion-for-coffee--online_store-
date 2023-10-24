from django import forms
from django.forms import TextInput, NumberInput

from address.models import Address


class AddressForm(forms.ModelForm):
    class Meta:
        model = Address
        exclude = ['user']

        widgets = {
            'street':TextInput(attrs={'class': 'form-control', 'placeholder': 'Please enter street name'}),
            'number':NumberInput(attrs={'class': 'form-control', 'placeholder': 'Please enter street number'}),
            'postal_cod':NumberInput(attrs={'class': 'form-control', 'placeholder': 'Please enter postal code'}),
            'city':TextInput(attrs={'class': 'form-control', 'placeholder': 'Please enter city name'}),
            'country':TextInput(attrs={'class': 'form-control', 'placeholder': 'Please enter country name'}),
            'phone_number':NumberInput(attrs={'class': 'form-control', 'placeholder': 'Please enter phone number'}),
        }