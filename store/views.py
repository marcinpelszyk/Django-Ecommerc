from django.shortcuts import render, get_object_or_404

from .models import Product
from category.models import Category


def store(request, slug=None):
    categories = None
    products = None

    if slug != None:
        categories = get_object_or_404(Category, slug=slug)
        products = Product.objects.filter(category=categories, is_avalible=True)
        product_count = products.count()
    else:
        products = Product.objects.all().filter(is_avalible=True)
        product_count = products.count()

    context = {
        'products': products,
        'product_count': product_count,
    }
    return render(request, 'store/store.html', context)

