from django.urls import path
from . import views

urlpatterns = [
    path('clothes/', views.Products, name='clothes'),
]