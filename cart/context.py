from django.conf import settings
from django.shortcuts import get_object_or_404
from menu.models import Menu_Item


def cart_contents(request):

    cart_items = []
    total = 0
    menu_item_count = 0
    cart = request.session.get('cart', {})

    for item_id, quantity in cart.items():
        menu_item = get_object_or_404(Menu_Item, pk=item_id)
        total += quantity * menu_item.price
        menu_item_count += quantity
        cart_items.append({
            'item_id': item_id,
            'quantity': quantity,
            'menu_item': menu_item,
        })

    if total < settings.FREE_DELIVERY_THRESHOLD:
        if total == 0:
            delivery = 0
            free_delivery_delta = 0
        else:
            delivery = settings.STANDARD_DELIVERY_AMOUNT
            free_delivery_delta = settings.FREE_DELIVERY_THRESHOLD - total
    else:
        delivery = 0
        free_delivery_delta = 0

    grand_total = delivery + total

    context = {
        'cart_items': cart_items,
        'total': total,
        'menu_item_count': menu_item_count,
        'delivery': delivery,
        'free_delivery_delta': free_delivery_delta,
        'free_delivery_threshold': settings.FREE_DELIVERY_THRESHOLD,
        'grand_total': grand_total,
    }

    return context
