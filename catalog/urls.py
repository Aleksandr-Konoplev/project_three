from catalog.apps import CatalogConfig
from django.urls import path

from catalog.views import ProductsListView, ProductDetailView, ContactsTemplateView

app_name = CatalogConfig.name

urlpatterns = [
    path("catalog/", ProductsListView.as_view(), name="product_list"),
    path(
        "catalog/product_detail/<int:pk>/",
        ProductDetailView.as_view(),
        name="product_detail",
    ),
    path("catalog/contacts/", ContactsTemplateView.as_view(), name="contacts"),
]
