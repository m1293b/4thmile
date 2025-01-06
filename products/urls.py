from django.urls import path
from . import views

urlpatterns = [
    path('clothes/', views.Products, name='clothes'),
    path('products/<int:pk>/', views.product_detail, name='product_detail'),  # Add this line for the detail view
]