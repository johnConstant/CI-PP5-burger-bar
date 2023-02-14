from django.contrib import admin
from .models import Location, Hours


class HoursAdminInline(admin.TabularInline):
    model = Hours


class LocationAdmin(admin.ModelAdmin):
    inlines = (HoursAdminInline,)
    prepopulated_fields = ({'slug': ('name',)})
    fields = ('name', 'slug',
              'email', 'phone_number', 'country',
              'postcode', 'town_or_city', 'street_address1',
              'street_address2', 'county', 'latitude',
              'longitude',)
    list_display = ('name', 'street_address1', 'phone_number')


admin.site.register(Location, Hours)
