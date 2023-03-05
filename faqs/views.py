from django.shortcuts import render
from django.views import generic, View
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required

from .models import FAQ
from .forms import FaqForm

class FAQList(generic.ListView):
    """
    A class view for getting all categories
    """
    model = FAQ
    queryset = FAQ.objects.all()
    template_name = 'faqs/faqs.html'


class FaqAdd(View):
    """
    A class view for adding a faq
    """
    @method_decorator(login_required)
    def get(self, request, *args, **kwargs):
        if not request.user.is_superuser:
            messages.error(request, 'Sorry, only store owners can do that.')
            return redirect(reverse('home'))

        form = FaqForm()
        context = {
            'form': form
        }
        return render(request, 'faqs/add_faq.html', context)

    @method_decorator(login_required)
    def post(self, request, *args, **kwargs):
        if not request.user.is_superuser:
            messages.error(request, 'Sorry, only store owners can do that.')
            return redirect(reverse('home'))
        try:
            form = FaqForm(request.POST, request.FILES)
            if form.is_valid():
                form.save()
                messages.success(request, "Your faq has been added.")
                return redirect('faqs')
            else:
                messages.error(request,
                               'Failed to add your faq. Please ensure the form\
                                 is valid.')
                form = FaqForm(request.POST, request.FILES)
                context = {
                    'form': form
                }
                return render(request, 'faqs/add_faq.html', context)
        except FAQ.DoesNotExist:
            messages.error(request,
                           'An error occurred when adding your faq.')
            return redirect('menu')

