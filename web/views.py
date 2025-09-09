from django.shortcuts import render

def home(request):
    return render(request, 'web/home.html')

def safari(request):
    return render(request, 'web/safari.html')

def about(request):
    return render(request, 'web/about.html')