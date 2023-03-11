from django.contrib import admin
from .models import UserProfile
from django_summernote.admin import SummernoteModelAdmin


@admin.register(UserProfile)
class UserProfileAdmin(SummernoteModelAdmin):

    list_display = ('user', )
    list_filter = ('default_location', )
    search_fields = ['name', 'email', ]
