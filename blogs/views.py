from django.shortcuts import render
from blogs.models import Blog


def show_description(request):
    blog = Blog.objects.all()
    content = {
        'blog': blog,
    }
    return render(request, 'blogs/description.html', content)


def show_covid(request):
    return render(request, 'blogs/covid.html')
