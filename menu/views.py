from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
# from django.utils.decorators import method_decorator
from django.db.models import Q
from django.views import generic, View
from django.db.models.functions import Lower
from django.template.defaultfilters import slugify
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from .models import Menu_Item, Menu_Category
from .forms import MenuItemForm


# Create your views here.

def MenuList(request):
    """
    A class view for getting all menu items
    """
    menu_items = Menu_Item.objects.filter(status=1).order_by('category')
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
            category = request.GET['category']
            menu_items = menu_items.filter(category__name=category)
            category = Menu_Category.objects.filter(name=category)

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

    current_sorting = f'{sort}_{direction}'

    page = request.GET.get('page', 1)
    paginator = Paginator(menu_items, 10)

    try:
        items = paginator.page(page)
    except PageNotAnInteger:
        items = paginator.page(1)
    except EmptyPage:
        items = paginator.page(paginator.num_pages)

    context = {
        "menu_items": items,
        "search": query,
        "current_category": category,
        "current_sorting": current_sorting
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


class MenuItemAdd(LoginRequiredMixin, View):
    """
    A class view for adding a menu item
    """
    def get(self, request, *args, **kwargs):
        if not request.user.is_superuser:
            messages.error(request, 'Sorry, only store owners can do that.')
            return redirect(reverse('home'))

        form = MenuItemForm()
        context = {
            'form': form
        }
        return render(request, 'menu/add_menu_item.html', context)

    # @method_decorator(login_required)
    def post(self, request, *args, **kwargs):
        if not request.user.is_superuser:
            messages.error(request, 'Sorry, only store owners can do that.')
            return redirect(reverse('home'))
        try:
            form = MenuItemForm(request.POST, request.FILES)
            form.instance.slug = slugify(request.POST['name'])
            if form.is_valid():
                form.save()
                messages.success(request, "Your item has been added.")
                return redirect('menu')
            else:
                messages.error(request,
                               'Failed to add your item. Please ensure the\
                                 form is valid.')
                form = MenuItemForm(request.POST, request.FILES)
                context = {
                    'form': form
                }
                return render(request, 'menu/add_menu_item.html', context)
        except Menu_Item.DoesNotExist:
            messages.error(request,
                           'An error occurred when adding your item.')
            return redirect('menu')


class MenuItemUpdate(LoginRequiredMixin, View):
    """
    A class view for updating an existing menu item
    """
    # @method_decorator(login_required)
    def get(self, request, slug, *args, **kwargs):
        if not request.user.is_superuser:
            messages.error(request, 'Sorry, only store owners can do that.')
            return redirect(reverse('home'))

        item = get_object_or_404(Menu_Item, slug=slug)
        form = MenuItemForm(instance=item)
        context = {
            'form': form
        }
        return render(request, 'menu/edit_menu_item.html', context)

    # @method_decorator(login_required)
    def post(self, request, slug, *args, **kwargs):
        if not request.user.is_superuser:
            messages.error(request, 'Sorry, only store owners can do that.')
            return redirect(reverse('home'))

        try:
            item = get_object_or_404(Menu_Item, slug=slug)
            form = MenuItemForm(request.POST, request.FILES, instance=item)
            form.instance.slug = slugify(request.POST['name'])
            if form.is_valid():
                form.save()
                messages.success(request, "Your item has been updated.")
                return redirect('menu')
            else:
                messages.error(request, "Please check that the information you\
                                entered is valid.")
                context = {
                    'form': form
                }
                return render(request, 'menu/edit_menu_item.html', context)
        except Menu_Item.DoesNotExist:
            messages.error(request,
                           'An error occurred when updating your item.')
            return redirect('menu')


class MenuItemDelete(LoginRequiredMixin, View):
    """
    A class view for deleting an existing menu item
    """
    # @method_decorator(login_required)
    def post(self, request, id, **kwargs):
        """
        Delete a selected menu item
        """
        if not request.user.is_superuser:
            messages.error(request, 'Sorry, only store owners can do that.')
            return redirect(reverse('home'))

        try:
            item = Menu_Item.objects.get(id=id)
            item.delete()
            messages.success(request, "Your item has been deleted.")
            return redirect('menu')
        except Menu_Item.DoesNotExist:
            messages.error(request,
                           'An error occurred when deleting your item.')
            return redirect('menu')
