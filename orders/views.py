from django.shortcuts import render

# Create your views here.

def Orders(request):
    return render(request, 'orders.html')