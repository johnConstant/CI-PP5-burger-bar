from django.shortcuts import render, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import UserProfile
from .forms import UserProfileForm
from checkout.forms import CommentForm
from checkout.models import Order


@login_required
def profile(request):
    """ Display the user's profile. """
    profile = get_object_or_404(UserProfile, user=request.user)
    orders = profile.orders.all()

    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request,
                             'Your profile has been updated successfully')
        else:
            messages.error(request,
                           'Please check that the information you entered\
                            is valid')
    else:
        form = UserProfileForm(instance=profile)

    # print(profile.user.default_location)

    template = 'profiles/profile.html'
    context = {
        'profile': profile,
        'orders': orders,
        'form': form,
    }

    return render(request, template, context)


@login_required
def order_history(request, order_number):
    if request.method == 'POST':
        order = get_object_or_404(Order, order_number=order_number)
        comments = order.comments.filter(approved=True).order_by(
            'created_date')

        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            comment_form.instance.email = request.user.email
            comment_form.instance.name = request.user.username
            comment = comment_form.save(commit=False)
            comment.order = order
            comment.save()
        else:
            comment_form = CommentForm()

        context = {
            'order': order,
            'comments': comments,
            'commented': True,
            'from_profile': True,
            'comment_form': CommentForm()
        }
        return render(request, 'profiles/prev_order.html', context)

    order = get_object_or_404(Order, order_number=order_number)
    comments = order.comments.filter(approved=True).order_by(
            'created_date')
    messages.info(request, (
        f'This is a past confirmation for order number {order_number}. '
        'A confirmation email was sent on the order date.'
    ))

    template = 'profiles/prev_order.html'
    context = {
        'order': order,
        'from_profile': True,
        'comment_form': CommentForm(),
        'comments': comments,
    }

    return render(request, template, context)
