from django.urls import path
from . import views

urlpatterns = [
    path('', views.show_shop, name='landing'),
    path('shop/', views.show_shop2, name='shop'),
]