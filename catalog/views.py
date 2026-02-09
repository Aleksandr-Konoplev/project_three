from django.core.exceptions import PermissionDenied
from django.core.cache import cache
from django.shortcuts import get_object_or_404, redirect

from django.views.generic import ListView, DetailView, TemplateView, View
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page

from catalog.models import Product, Category
from catalog.forms import ProductForm
from catalog.services import ProductService


# Просмотр товаров
class ProductsListView(ListView):
    model = Product
    template_name = "catalog/product_list.html"
    context_object_name = "products"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        context['current_category'] = None
        return context

    def get_queryset(self):
        user = self.request.user
        cache_key = f"products_list_user_{user.id if user.is_authenticated else 'anon'}"
        products = cache.get(cache_key)

        if products is None:
            queryset = Product.objects.all()

            if not user.has_perm('catalog.can_unpublish_product'):
                published = queryset.filter(is_published=True)

                if user.is_authenticated:
                    owner_prod = queryset.filter(owner=user)
                    queryset = published | owner_prod
                else:
                    queryset = published

            products = list(queryset)
            cache.set(cache_key, products, timeout=60 * 5)

        return products


class ProductsByCategoryView(ListView):
    template_name = "catalog/products_by_category.html"
    context_object_name = "products"

    def get_queryset(self):
        category_id = self.kwargs["category_id"]
        return ProductService.selected_category(category_id)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["category"] = Category.objects.get(id=self.kwargs["category_id"])
        context["categories"] = Category.objects.all()
        return context


@method_decorator(cache_page(60 * 15), name='dispatch')
class ProductDetailView(LoginRequiredMixin, DetailView):
    model = Product
    template_name = "catalog/product_detail.html"
    context_object_name = "product"


# Создание товара
class ProductCreateView(LoginRequiredMixin, CreateView):
    model = Product
    form_class = ProductForm
    template_name = "catalog/form_product.html"
    success_url = reverse_lazy("catalog:product_list")

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)


# Обновление (изменение) товара
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


# Удаление товара
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
