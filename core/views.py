from django.shortcuts import render
from store.models import Product

def index(request):
    products = Product.objects.all().filter(is_avalible=True)
    return render(request, 'core/index.html', {'products': products})

