from django.shortcuts import render, get_object_or_404
from django.views import generic, View

from .models import Location


class LocationList(generic.ListView):
    """
    A class view for getting all categories
    """
    model = Location
    queryset = Location.objects.all()
    template_name = 'locations/locations.html'


class LocationDetail(View):
    """
    A class view for getting a specific location
    """
    def get(self, request, slug, *args, **kwargs):
        queryset = Location.objects.all()
        location = get_object_or_404(queryset, slug=slug)
        days = Location.objects.filter(opening_hours=location.id)
        print(days)
        context = {
            'location': location,
            'days': days
        }
        return render(request, 'locations/location_detail.html', context)
