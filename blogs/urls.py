from django.urls import path
from . import views

urlpatterns = [
    path('description/', views.show_description, name='description'),
    path('covid19/', views.show_covid, name='covid19'),
]