from django.shortcuts import render

from menu.models import Menu_Item


def index(request):
    """ A view to return the index page """
    special = Menu_Item.objects.filter(featured=True)[:1]

    context = {
        'specials': special
    }

    return render(request, 'home/index.html', context)


def privacy_policy(request):
    """ A view to return the privacy policy page """

    return render(request, 'home/privacy_policy.html')
