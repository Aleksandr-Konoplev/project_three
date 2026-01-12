from django.shortcuts import get_object_or_404, redirect

from catalog.models import Product
from catalog.forms import ProductForm

from django.views.generic import ListView, DetailView, TemplateView, View
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.urls import reverse_lazy


class ProductsListView(ListView):
    model = Product
    template_name = "catalog/product_list.html"
    context_object_name = "products"

    def get_queryset(self):
        queryset = Product.objects.all()

        # обычные пользователи видят только опубликованные
        if not self.request.user.has_perm('catalog.can_unpublish_product'):
            queryset = queryset.filter(is_published=True)

        return queryset


class ProductDetailView(LoginRequiredMixin, DetailView):
    model = Product
    template_name = "catalog/product_detail.html"
    context_object_name = "product"


class ProductCreateView(LoginRequiredMixin, CreateView):
    model = Product
    form_class = ProductForm
    template_name = "catalog/form_product.html"
    success_url = reverse_lazy("catalog:product_list")


class ProductUpdateView(LoginRequiredMixin, UpdateView):
    model = Product
    form_class = ProductForm
    template_name = "catalog/form_product.html"
    success_url = reverse_lazy("catalog:product_list")


class ProductDeleteView(LoginRequiredMixin, DeleteView):
    model = Product
    template_name = "catalog/confirm_delete.html"
    success_url = reverse_lazy("catalog:product_list")


class TogglePublication(LoginRequiredMixin, PermissionRequiredMixin, View):
    permission_required = 'catalog.can_unpublish_product'

    @staticmethod
    def post(request, pk):
        product = get_object_or_404(Product, pk=pk)

        product.is_published = not product.is_published
        product.save(update_fields=['is_published'])

        return redirect('catalog:product_list')


class ContactsTemplateView(TemplateView):
    template_name = "catalog/contacts.html"
