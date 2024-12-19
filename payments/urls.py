from django.urls import path
from . import views

urlpatterns = [
    path('checkout/<order_id>/', views.StripeCheckoutView.as_view(), name='checkout'),
]