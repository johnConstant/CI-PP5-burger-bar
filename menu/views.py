from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from django.views import generic, View

from .models import Menu_Item, Menu_Category, Special_Offer


# Create your views here.

def MenuList(request):
    """
    A class view for getting all menu items
    """
    menu_items = Menu_Item.objects.all()
    # paginate_by = 15
    query = None

    if request.GET:
        if 'search' in request.GET:
            query = request.GET['search']
            if not query:
                messages.error(request, "You didn't enter any search criteria!")
                return redirect(reverse('products'))

            queries = Q(name__icontains=query) | Q(description__icontains=query)
            menu_items = menu_items.filter(queries)

    context = {
        "menu_items": menu_items,
        "search": query
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
