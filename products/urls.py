from django.urls import path
from .views import Products, Clothes, product_detail, add_product, search_products

urlpatterns = [
    path("products/", Products, name="products_list"),
    path("clothes/", Clothes, name="clothes_list"),
    path("add_product/", add_product, name="add_product"),
    path("search_products/", search_products, name="search_products"),
    path("products/<int:pk>/", product_detail, name="product_detail"),
]
