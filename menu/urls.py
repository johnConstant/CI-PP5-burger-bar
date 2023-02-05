from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.MenuList, name='menu'),
    path('<slug:slug>', views.MenuItemDetail.as_view(), name='menu_detail'),
]
