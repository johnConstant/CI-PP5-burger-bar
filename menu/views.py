from django.shortcuts import render
from django.views import generic, View

from .models import Menu_Item, Menu_Category, Special_Offer


# Create your views here.
class MenuList(generic.ListView):
    """
    A class view for getting a specific category
    """
    def get(self, request, *args, **kwargs):
        items = Menu_Item.objects.all()
        categories = Menu_Category.objects.all()

        context = {
            'items': items,
            'categories': categories
        }

        return render(request, 'menu/menu.html', context)
