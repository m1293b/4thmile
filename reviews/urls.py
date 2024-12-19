from django.urls import path
from . import views

urlpatterns = [
    path('reviews/', views.Reviews, name='reviews'),
]