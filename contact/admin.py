from django.contrib import admin
from .models import Contact
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Contact)
class ContactAdmin(SummernoteModelAdmin):

    list_display = ('name', 'email', 'message')
    list_filter = ('email_subscription',)
    search_fields = ['name', 'email', 'message']
    summernote_fields = ('message',)
