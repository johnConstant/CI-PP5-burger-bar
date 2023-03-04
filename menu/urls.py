from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.MenuList, name='menu'),
    path(
         'add/', views.MenuItemAdd.as_view(), name='add_menu_item'
    ),
    path('<slug:slug>', views.MenuItemDetail.as_view(), name='menu_detail'),
]
