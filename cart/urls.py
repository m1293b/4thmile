from django.urls import path
from . import views


# to be updated
urlpatterns = [
    path('cart/', views.Cart, name='cart'),
]