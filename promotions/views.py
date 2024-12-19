from django.shortcuts import render

# Create your views here.

def Promotions(request):
    return render(request, 'promotions.html')