from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.FAQList.as_view(), name='faqs'),
    path(
         'add/', views.FaqAdd.as_view(), name='add_faq'
    ),
]
