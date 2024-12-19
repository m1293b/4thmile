from django.urls import path
from . import views

urlpatterns = [
    path('shipping/', views.Shipping, name='shipping'),
]