from django.shortcuts import render, get_object_or_404

from catalog.models import Product

from django.views.generic import ListView, DetailView, TemplateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView


def index(request):
    return render(request, 'base.html')


class ProductsListView(ListView):
    model = Product
    template_name = 'product_list.html'
    context_object_name = 'products'


class ProductDetailView(DetailView):
    model = Product
    template_name = 'product_detail.html'
    context_object_name = 'product'


class ContactsTemplateView(TemplateView):
    template_name = 'contacts.html'