from django.shortcuts import render, get_object_or_404
from blogs.models import Blog
from products.models import Product


def show_description(request):
    blog = Blog.objects.all()
    content = {
        'blog': blog,
    }
    return render(request, 'blogs/description.html', content)


def show_covid(request):
    return render(request, 'blogs/covid.html')


def show_slider(request):
    product = get_object_or_404(Product, id=5)
    content = {
        'product': product,
    }
    return render(request, 'blogs/slider.html', content)
