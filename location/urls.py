from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.LocationList.as_view(), name='locations'),
    path(
         'add/', views.LocationAdd.as_view(), name='add_location'
    ),
    path(
         'edit/<slug:slug>/', views.LocationUpdate.as_view(), name='edit_location'
    ),
    path(
        '<slug:slug>/', views.LocationDetail.as_view(), name='location_detail'
    ),
]
