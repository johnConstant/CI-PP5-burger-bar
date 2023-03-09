from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('about/', views.about, name='about'),
    path('sitemap', views.sitemap, name='sitemap'),
    path('privacy-policy/', views.privacy_policy, name='privacy_policy')
]
