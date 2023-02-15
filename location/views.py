from django.shortcuts import render
from django.views import generic

from .models import Location


class LocationList(generic.ListView):
    """
    A class view for getting all categories
    """
    model = Location
    queryset = Location.objects.all()
    template_name = 'locations/locations.html'
