from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    # path('safari/', views.safari, name='safari'),
    path('about/', views.about, name='about'),
    path('destinations/', views.destinations, name='destination'),
    path('destination/<slug:slug>/', views.destination, name='destination'),
    path('safaris/', views.safaris, name='safaris'),
    path('safari/<slug:slug>/', views.safari, name='safari'),
    path('blog/', views.articles, name='blog'),
    path('blog/<slug:slug>/', views.article, name='article'),
    
]
