from django.shortcuts import render

# Create your views here.

def Report(request):
    return render(request, 'analytics/report.html')