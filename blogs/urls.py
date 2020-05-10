from django.urls import path
from . import views

urlpatterns = [
    path('responsecode/', views.show_description, name='responsecode'),
    path('covid19/', views.show_covid, name='covid19'),
]