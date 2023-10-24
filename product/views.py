from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render

from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, UpdateView, DeleteView, DetailView

from product.forms import ProductForm, ProductUpdateForm
from product.models import Product


class ProductCreateView(LoginRequiredMixin, CreateView):
    template_name = 'product/create_product.html'
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy('home_page')


class ProductListView(LoginRequiredMixin, ListView):
    template_name = 'product/list_of_products.html'
    model = Product
    context_object_name = 'all_products'



class ProductUpdateView(LoginRequiredMixin, UpdateView):
    template_name = 'product/update_product.html'
    model = Product
    form_class = ProductUpdateForm
    success_url = reverse_lazy('list_of_products')

class ProductDeleteView(LoginRequiredMixin, DeleteView):
    template_name = 'product/delete_product.html'
    model = Product
    success_url = reverse_lazy('list_of_products')

class ProductDetailView(LoginRequiredMixin, DetailView):
    template_name = 'product/detail_product.html'
    model = Product


def get_all_products_per_category(request, pk):
    products_per_category = Product.objects.filter(category_id=pk)
    return render(request, 'product/product_per_category.html', {'products_category': products_per_category} )