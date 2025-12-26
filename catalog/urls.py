from catalog.apps import CatalogConfig
from django.urls import path

from catalog.views import ProductsListView, ProductDetailView, ContactsTemplateView, ProductCreateView, ProductUpdateView, ProductDeleteView

app_name = CatalogConfig.name

urlpatterns = [
    path("catalog/", ProductsListView.as_view(), name="product_list"),
    path(
        "catalog/product/<int:pk>/detail/",
        ProductDetailView.as_view(),
        name="product_detail",
    ),
    path("catalog/product/add/", ProductCreateView.as_view(), name="add_product"),
    path("catalog/product/<int:pk>/update/", ProductUpdateView.as_view(), name="update_product"),
    path("catalog/product/<int:pk>/delete/", ProductDeleteView.as_view(), name="delete_product"),

    path("catalog/contacts/", ContactsTemplateView.as_view(), name="contacts"),
]
