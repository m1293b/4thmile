from django.urls import path
from . import views
from products.views import products, product_detail

urlpatterns = [
    path("reviews/", views.Reviews, name="reviews"),
    path("products/<int:pk>/", product_detail, name="product_detail"),
]
