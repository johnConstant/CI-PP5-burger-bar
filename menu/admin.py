from django.contrib import admin
from .models import Menu_Category, Menu_Item, Special_Offer
from django_summernote.admin import SummernoteModelAdmin


# Register your models here.


@admin.register(Menu_Item)
class MenuItemAdmin(SummernoteModelAdmin):
    prepopulated_fields = ({'slug': ('name',)})
    list_display = ('name', 'description', 'price')
    search_fields = ['name', 'description', 'categories']
    summernote_fields = ('description')


@admin.register(Menu_Category)
class MenuCategoryAdmin(SummernoteModelAdmin):
    prepopulated_fields = ({'slug': ('name',)})
    list_display = ('name', 'description')
    search_fields = ['name',]
    summernote_fields = ('description')


@admin.register(Special_Offer)
class SpecialOfferAdmin(SummernoteModelAdmin):
    prepopulated_fields = ({'slug': ('name',)})
    list_display = ('name', 'description', 'price')
    search_fields = ['name',]
    summernote_fields = ('description')
