from django.urls import path
from . import views

urlpatterns = [
    path('process-payment/', views.process_payment, name='process_payment'),
    path('success/', views.success, name='success'),
    path('profile/', views.profile, name='profile'),
]
