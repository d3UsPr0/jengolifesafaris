from django.shortcuts import get_object_or_404, render
from .models import Destination

def home(request):
    # Get all destinations or filter as needed
    destinations = Destination.objects.filter(is_popular=True)  # or .all() for all destinations
    
    context = {
        'destinations': destinations
    }
    return render(request, 'web/home.html', context)


def destination(request, slug):
    # Get the destination by slug or return 404
    destination = get_object_or_404(Destination, slug=slug)

    context = {
        'destination': destination
    }
    return render(request, 'web/destination.html', context)


def safari(request):
    return render(request, 'web/safari.html')

def about(request):
    return render(request, 'web/about.html')

def destinations(request):
    # Get all destinations or filter as needed
    destinations = Destination.objects.filter(is_popular=True)  # or .all() for all destinations
    
    context = {
        'destinations': destinations
    }
    return render(request, 'web/destinations.html', context)

