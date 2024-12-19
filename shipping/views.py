from django.shortcuts import render

# Create your views here.

def Shipping(request):
    return render(request, 'shipping.html')