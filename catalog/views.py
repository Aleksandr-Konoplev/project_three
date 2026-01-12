from django.core.exceptions import PermissionDenied
from django.shortcuts import get_object_or_404, redirect

from django.views.generic import ListView, DetailView, TemplateView, View
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.urls import reverse_lazy

from catalog.models import Product
from catalog.forms import ProductForm


class ProductsListView(ListView):
    model = Product
    template_name = "catalog/product_list.html"
    context_object_name = "products"

    def get_queryset(self):
        user = self.request.user
        queryset = Product.objects.all()

        if not user.has_perm('catalog.can_unpublish_product'):
            published = queryset.filter(is_published=True)
            owner_prod = queryset.filter(owner=user)
            queryset = published | owner_prod

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

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)


class ProductUpdateView(LoginRequiredMixin, UpdateView):
    model = Product
    form_class = ProductForm
    template_name = "catalog/form_product.html"
    success_url = reverse_lazy("catalog:product_list")

    def dispatch(self, request, *args, **kwargs):
        product = self.get_object()

        if product.owner == request.user or request.user.has_perm('catalog.can_unpublish_product'):
            return super().dispatch(request, *args, **kwargs)

        raise PermissionDenied("Вы не можете редактировать этот товар.")


class ProductDeleteView(LoginRequiredMixin, DeleteView):
    model = Product
    template_name = "catalog/confirm_delete.html"
    success_url = reverse_lazy("catalog:product_list")

    def dispatch(self, request, *args, **kwargs):
        product = self.get_object()

        if product.owner == request.user or request.user.has_perm('catalog.can_unpublish_product'):
            return super().dispatch(request, *args, **kwargs)

        raise PermissionDenied("Вы не можете редактировать этот товар.")


class TogglePublication(LoginRequiredMixin, PermissionRequiredMixin, View):
    permission_required = 'catalog.can_unpublish_product'

    @staticmethod
    def post(request, pk):
        product = get_object_or_404(Product, pk=pk)

        if product.owner == request.user or request.user.has_perm('catalog.can_unpublish_product'):
            product.is_published = not product.is_published
            product.save(update_fields=['is_published'])
            return redirect('catalog:product_list')

        raise PermissionDenied("Вы не можете редактировать этот товар.")


class ContactsTemplateView(TemplateView):
    template_name = "catalog/contacts.html"
