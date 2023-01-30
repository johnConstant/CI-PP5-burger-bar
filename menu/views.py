from django.shortcuts import render, get_object_or_404
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


class MenuItemDetail(View):
    """
    A class view for getting a specific menu item
    """
    def get(self, request, slug, *args, **kwargs):
        queryset = Menu_Item.objects.all()
        item = get_object_or_404(queryset, slug=slug)

        context = {
            'item': item,
        }
        return render(request, 'menu/menu_detail.html', context)
