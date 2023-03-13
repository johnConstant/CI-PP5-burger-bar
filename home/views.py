from django.shortcuts import render

from menu.models import Menu_Item


def index(request):
    """ A view to return the index page """
    special = Menu_Item.objects.filter(featured=True)[:3]

    context = {
        'specials': special
    }

    return render(request, 'home/index.html', context)


def about(request):
    """ A view to return the about us page """

    return render(request, 'home/about_us.html')


def sitemap(request):
    """ A view to return the sitemap us page """

    return render(request, 'home/sitemap.html')


def privacy_policy(request):
    """ A view to return the privacy policy page """

    return render(request, 'home/privacy_policy.html')
