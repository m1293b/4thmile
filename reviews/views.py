from django.shortcuts import render

# Create your views here.

def Reviews(request):
    return render(request, 'reviews.html')