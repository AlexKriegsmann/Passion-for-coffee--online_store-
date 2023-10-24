from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, UpdateView, DeleteView, DetailView

from category.forms import CategoryForm, CategoryUpdateForm
from category.models import Category


class CategoryCreateView(LoginRequiredMixin, CreateView):
    template_name = 'category/create_category.html'
    model = Category
    form_class = CategoryForm
    success_url = reverse_lazy('home_page')


class CategoryListView(LoginRequiredMixin, ListView):
    template_name = 'category/list_of_categories.html'
    model = Category
    context_object_name = 'all_categories'




class CategoryUpdateView(LoginRequiredMixin, UpdateView):
    template_name = 'category/update_category.html'
    model = Category
    form_class = CategoryUpdateForm
    success_url = reverse_lazy('list_of_categories')

class CategoryDeleteView(LoginRequiredMixin, DeleteView):
    template_name = 'category/delete_category.html'
    model = Category
    success_url = reverse_lazy('list_of_categories')

class CategoryDetailView(LoginRequiredMixin, DetailView):
    template_name = 'category/detail_category.html'
    model = Category






