from django.shortcuts import render, get_object_or_404

from catalog.models import Product


def index(request):
    return render(request, 'base.html')


def product_list(request):
    products = Product.objects.all()
    context = {
        'products': products
    }
    return render(request, 'product_list.html', context=context)


def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    context = {
        'product': product
    }
    return render(request, 'product_detail.html', context=context)