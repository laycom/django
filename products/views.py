from django.shortcuts import render
from products.models import *
from django.shortcuts import get_object_or_404


def all_products(request):
    product_images = ProductImage.objects.filter(is_active=True, is_main=True)
    content = {
        'product_images': product_images,
    }
    return render(request, 'product/all_products.html', content)


def product(request, product_id):
    session_key = request.session.session_key
    if not session_key:
        request.session.cycle_key
    print(session_key)
    product = get_object_or_404(Product, id=product_id)
    content = {
        'product': product,
    }
    return render(request, 'product/product.html', content)
