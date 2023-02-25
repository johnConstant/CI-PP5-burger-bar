from django.shortcuts import render, redirect, reverse
from django.contrib import messages
import os
import env

from .forms import OrderForm


def checkout(request):
    cart = request.session.get('cart', {})
    if not cart:
        messages.error(request, "You haven't ordered anything yet! ")
        return redirect(reverse('menu'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': os.environ.get('STRIPE_SECRET_KEY'),
        'client_secret': os.environ.get('STRIPE_CLIENT_SECRET'),
    }

    return render(request, template, context)
