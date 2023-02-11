from django.shortcuts import render
from django.views import generic

from .models import FAQ


class FAQList(generic.ListView):
    """
    A class view for getting all categories
    """
    model = FAQ
    queryset = FAQ.objects.all()
    template_name = 'faqs/faqs.html'
