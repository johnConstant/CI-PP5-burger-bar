from django.shortcuts import render, redirect
from django.views import generic, View
from django.contrib import messages

from .forms import ContactForm
from profiles.forms import UserProfile


class Contact(View):
    """
    A class view for the contact page
    """
    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            try:
                profile = UserProfile.objects.get(user=request.user)
                contact_form = ContactForm(initial={
                    'name': profile.user.username,
                    'email': profile.user.email
                })
            except UserProfile.DoesNotExist:
                contact_form = ContactForm()
        else:
            contact_form = ContactForm()

        context = {
            'contact_form': contact_form
        }
        return render(request, 'contact/contact.html', context)

    def post(self, request, *args, **kwargs):
        contact_form = ContactForm(request.POST)
        if contact_form.is_valid():
            contact_form.save()
            messages.success(request, "Your message has been sent.")
            return redirect('/')
