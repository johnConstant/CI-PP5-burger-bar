from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from django.views import generic, View
from django.db.models.functions import Lower

from .models import Menu_Item, Menu_Category, Special_Offer


# Create your views here.

def MenuList(request):
    """
    A class view for getting all menu items
    """
    menu_items = Menu_Item.objects.all()
    # paginate_by = 15
    query = None
    category = None
    sort = None
    direction = None

    if request.GET:
        if 'sort' in request.GET:
            sortkey = request.GET['sort']
            sort = sortkey
            if sortkey == 'name':
                sortkey = 'lower_name'
                menu_items = menu_items.annotate(lower_name=Lower('name'))
            if sortkey == 'category':
                sortkey = 'category__name'
            if 'direction' in request.GET:
                direction = request.GET['direction']
                if direction == 'desc':
                    sortkey = f'-{sortkey}'
            menu_items = menu_items.order_by(sortkey)

        if 'category' in request.GET:
            categories = request.GET['category'].split(',')
            menu_items = menu_items.filter(category__name__in=categories)
            categories = Menu_Category.objects.filter(name__in=categories)

        if 'search' in request.GET:
            query = request.GET['search']
            if not query:
                messages.error(
                    request, "You didn't enter any search criteria!"
                    )
                return redirect(reverse('menu'))

            queries = (
                Q(name__icontains=query) | Q(description__icontains=query)
                )
            menu_items = menu_items.filter(queries)

    context = {
        "menu_items": menu_items,
        "search": query,
        "current_category": categories,
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
