from django.shortcuts import render
from .forms import SubscriberForm
from products.models import Product, ProductImage


def home(request):
    products = Product.objects.filter(is_active=True)
    product_images = ProductImage.objects.filter(is_active=True, is_main=True)
    content = {
        'products': products,
        'product_images': product_images,
    }
    return render(request, 'landing/home.html', content)


def show_shop2(request):
    form = SubscriberForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        form.save()
    return render(request, 'landing/shop.html', locals())
