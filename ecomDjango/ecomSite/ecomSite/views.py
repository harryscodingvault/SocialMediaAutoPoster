from django.shortcuts import render
from store.models import Product

def home(request):
    products = Product.objects.all().filter(is_available=True)
    context = {
        'products': products,
    }

    return render(request, 'index/index.html', context=context)


def error_404_view(request, exception):
    return render(request, 'errors/404.html')


def error_500_view(request):
    return render(request, 'errors/500.html')
