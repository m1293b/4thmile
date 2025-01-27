from django.http import JsonResponse
from django.shortcuts import render
from cart.models import Cart, CartItem
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# Create your views here.

def home(request):
    return render(request, "home/home.html")


def about(request):
    return render(request, "home/about.html")


def contact(request):
    return render(request, "home/contact.html")
