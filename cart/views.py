from django.shortcuts import (
    render, redirect, reverse, HttpResponse, get_object_or_404
)
from django.contrib import messages

from menu.models import Menu_Item
# Create your views here.


def view_cart(request):
    """ A view to return the shopping cart page """

    return render(request, 'cart/cart.html')


def add_to_cart(request, item_id):
    """ Add a quantity of the specified product to the shopping cart """
    item = get_object_or_404(Menu_Item, pk=item_id)
    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    cart = request.session.get('cart', {})

    if item_id in list(cart.keys()):
        cart[item_id] += quantity
        messages.success(
            request, f'Updated quantity of {item.name} in your order'
            )
    else:
        cart[item_id] = quantity
        messages.success(request, f'{item.name} has been added to your order')

    request.session['cart'] = cart
    return redirect(redirect_url)


def adjust_cart(request, item_id):
    """Adjust the quantity of the specified product to the specified amount"""
    item = get_object_or_404(Menu_Item, pk=item_id)
    quantity = int(request.POST.get('quantity'))
    cart = request.session.get('cart', {})
    if quantity > 0:
        cart[item_id] = quantity
        messages.success(
            request, f'Updated quantity of {item.name} in your order'
            )
    else:
        cart.pop(item_id)
        messages.success(
            request, f'{item.name} has been removed from your order'
            )

    request.session['cart'] = cart
    return redirect(reverse('view_cart'))


def remove_from_cart(request, item_id):
    """Remove the item from the shopping cart"""
    try:
        item = get_object_or_404(Menu_Item, pk=item_id)
        cart = request.session.get('cart', {})
        cart.pop(item_id)
        messages.success(
            request, f'{item.name} has been removed from your order'
            )
        request.session['cart'] = cart
        return HttpResponse(status=200)

    except Exception as e:
        messages.error(request, f'Error removing {item.name}: {e}')
        return HttpResponse(status=500)
