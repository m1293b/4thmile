from django.urls import path
from .views import products, product_detail
from reviews.views import add_review, remove_review

urlpatterns = [
    path("", products, name="products"),
    path("<int:pk>/", product_detail, name="product_detail"),
    path("reviews/add/<int:pk>/", add_review, name="add_review"),
    path("reviews/remove/<int:pk>/", remove_review, name="remove_review"),
]
