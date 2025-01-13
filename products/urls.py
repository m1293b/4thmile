from django.urls import path
from .views import products, product_detail, add_product

urlpatterns = [
    path("", products, name="products"),
    path("add_product/", add_product, name="add_product"),
    path("<int:pk>/", product_detail, name="product_detail"),
]
