from django.urls import path
from . import views


# to be updated
urlpatterns = [
    path("", views.cart_summary, name="cart_summary"),
    path("add/", views.add_to_cart, name="add_to_cart"),
    path("update/", views.update_cart, name="update_cart"),
    path("remove/", views.remove_from_cart, name="remove_from_cart"),
    path("clear-all-carts/", views.clear_all_carts, name="clear_all_carts"),
    path("checkout/", views.checkout, name="checkout"),
]
