from django.shortcuts import render, redirect, get_object_or_404
from django.views import generic, View
from django.contrib import messages
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required

from .models import Location
from .forms import LocationForm


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


class LocationAdd(View):
    """
    A class view for adding a new location
    """
    @method_decorator(login_required)
    def get(self, request, *args, **kwargs):
        if not request.user.is_superuser:
            messages.error(request, 'Sorry, only store owners can do that.')
            return redirect(reverse('home'))

        form = LocationForm()
        context = {
            'form': form
        }
        return render(request, 'locations/add_location.html', context)

    @method_decorator(login_required)
    def post(self, request, *args, **kwargs):
        if not request.user.is_superuser:
            messages.error(request, 'Sorry, only store owners can do that.')
            return redirect(reverse('home'))
        try:
            form = LocationForm(request.POST, request.FILES)
            form.instance.slug = slugify(request.POST['name'])
            if form.is_valid():
                form.save()
                messages.success(request, "Your location has been added.")
                return redirect('locations')
            else:
                messages.error(request,
                               'Failed to add your location. Please ensure the form\
                                 is valid.')
                form = LocationForm(request.POST, request.FILES)
                context = {
                    'form': form
                }
                return render(request, 'locations/add_location.html', context)
        except Location.DoesNotExist:
            messages.error(request,
                           'An error occurred when adding your location.')
            return redirect('locations')
