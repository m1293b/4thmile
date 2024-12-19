from django.urls import path
from . import views

urlpatterns = [
    path("promortions/", views.Promotions, name="promotions"),
]