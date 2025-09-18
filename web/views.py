from django.utils import timezone
from django.shortcuts import get_object_or_404, render
from .models import FAQ, BlogPost, Destination, SafariPackage, Testimonial

def home(request):
    # Get all destinations or filter as needed
    destinations = Destination.objects.filter(is_popular=True)
    safari_packages = SafariPackage.objects.filter(is_featured=True)
    testimonials = Testimonial.objects.filter(is_featured=True).order_by('-created_at')[:3]
    faqs = FAQ.objects.filter(is_active=True).order_by('order', 'question')
    articles = BlogPost.objects.filter(
        is_published=True,
        published_date__lte=timezone.now()
    ).order_by('-published_date')
    
    context = {
        'destinations': destinations,
        'safari_packages': safari_packages,
        'testimonials': testimonials,
        'faqs': faqs,
        'articles': articles,
    }
    return render(request, 'web/home.html', context)

def destination(request, slug):
    # Get the destination by slug or return 404
    destination = get_object_or_404(Destination, slug=slug)

    context = {
        'destination': destination
    }
    return render(request, 'web/destination.html', context)

def destinations(request):
    # Get all destinations or filter as needed
    destinations = Destination.objects.filter(is_popular=True)  # or .all() for all destinations
    
    context = {
        'destinations': destinations
    }
    return render(request, 'web/destinations.html', context)



def safari(request, slug):
    # Get a single safari package detail
    safari_package = get_object_or_404(SafariPackage, slug=slug)
    
    context = {
        'safari_package': safari_package
    }
    return render(request, 'web/safari.html', context)
def safaris(request):
    # List all safari packages
    safari_packages = SafariPackage.objects.all()
    
    context = {
        'safari_packages': safari_packages
    }
    return render(request, 'web/safaris.html', context)

def about(request):
    return render(request, 'web/about.html')

def articles(request):
    articles = BlogPost.objects.filter(
        is_published=True,
        published_date__lte=timezone.now()
    ).order_by('-published_date')
    
    context = {
        'articles': articles
    }
    return render(request, 'web/articles.html', context)

def article(request, slug):
    # Get the article by slug or return 404
    article = get_object_or_404(BlogPost, slug=slug)

    context = {
        'article': article
    }
    return render(request, 'web/article.html', context)

