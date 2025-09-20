from django.utils import timezone
from .models import BlogPost, SiteSetting

def global_context(request):
    """Makes these variables available in all templates"""
    settings = SiteSetting.objects.first()
    articles = BlogPost.objects.filter(
        is_published=True,
        published_date__lte=timezone.now()
    ).order_by('-published_date')


    return {
        'settings': settings,
        'articles': articles
    }