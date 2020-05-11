from django.shortcuts import render
from .forms import SubscriberForm
from products.models import Product, ProductImage


def home(request):
    product_images = ProductImage.objects.filter(is_active=True, is_main=True, product__is_active=True)
    product_images_phones = product_images.filter(product__category__name='phone')
    product_images_laptops = product_images.filter(product__category__name='laptop')
    content = {
        'product_images': product_images[:4],
        'product_images_phones': product_images_phones[:4],
        'product_images_laptops': product_images_laptops[:4],
    }
    return render(request, 'landing/home.html', content)



