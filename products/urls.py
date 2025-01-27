from django.urls import path
from .views import products, product_detail
from reviews.views import add_review, review_list

urlpatterns = [
    path("", products, name="products"),
    path("<int:pk>/", product_detail, name="product_detail"),
    # Add the following line to include the reviews URLs // are these working?
    path("reviews/list/<int:pk>/", review_list, name="review_list"),
    path("reviews/add/<int:pk>/", add_review, name="add_review"),
]
