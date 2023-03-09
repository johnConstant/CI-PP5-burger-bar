from django.contrib import admin
from .models import Menu_Category, Menu_Item, Allergen
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


@admin.register(Allergen)
class AllergensAdmin(SummernoteModelAdmin):
    list_display = ('name', 'description', 'icon')
    search_fields = ['name',]
    summernote_fields = ('description')
