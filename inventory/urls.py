from django.urls import path
from . import views

urlpatterns = [
    path('inventory/', views.Inventory, name='inventory'),
]