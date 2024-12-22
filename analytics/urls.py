from django.urls import path
from . import views


# to be updated
urlpatterns = [
    path('report/', views.Report, name='report'),
]