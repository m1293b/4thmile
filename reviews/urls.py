from django.urls import path
from . import views
from products.views import products, product_detail

urlpatterns = [
    path("", views.Reviews, name="reviews"),
]
