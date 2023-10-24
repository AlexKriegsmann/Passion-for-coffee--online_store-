from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView

from address.forms import AddressForm
from address.models import Address


class AddressCreateView(CreateView):
    template_name = 'address/create_address.html'
    model = Address
    form_class = AddressForm
    success_url = reverse_lazy('home_page')

    def form_valid(self, form):
        new_address = form.save(commit=False)
        new_address.user_id = self.request.user.id
        new_address.save()

        return redirect('create_address')

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        addresses_per_user = Address.objects.filter(user_id=self.request.user.id)
        data['all_addresses'] = addresses_per_user
        return data



