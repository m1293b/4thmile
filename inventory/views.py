from django.shortcuts import render

# Create your views here.

def Inventory(request):
    return render(request, 'inventory.html')