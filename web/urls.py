from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('safari/', views.safari, name='safari'),
    path('about/', views.about, name='about'),
    path('destinations/', views.destinations, name='destination'),
    path('destination/<slug:slug>/', views.destination, name='destination'),
]
