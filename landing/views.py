from django.shortcuts import render
from .forms import SubscriberForm


def show_shop(request):
    form = SubscriberForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        form.save()
    return render(request, 'landing/landing.html', locals())

def show_shop2(request):
    form = SubscriberForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        form.save()
    return render(request, 'landing/shop.html', locals())
