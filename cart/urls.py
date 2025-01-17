from django.urls import path
from . import views


# to be updated
urlpatterns = [
    path("", views.cart_summary, name="cart"),
    path("add/", views.add_to_cart, name="add_to_cart"),
    path("update/", views.update_cart, name="update_cart"),
    path("remove/", views.remove_from_cart, name="remove_from_cart"),
]
