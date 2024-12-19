from django.shortcuts import render

# Create your views here.

def Notification(request):
    return render(request, 'notifications.html')