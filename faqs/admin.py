from django.contrib import admin
from .models import FAQ
from django_summernote.admin import SummernoteModelAdmin

# Register your models here.


@admin.register(FAQ)
class FAQAdmin(SummernoteModelAdmin):

    list_display = ('question', 'answer')
    search_fields = ['question', 'answer']
    summernote_fields = ('question', 'answers')
