from django.db import models
from profiles.models import UserProfile


class Contact(models.Model):
    """
    A class for the Contact model
    """
    name = models.CharField(max_length=200)
    user_profile = models.ForeignKey(
        UserProfile, on_delete=models.SET_NULL,
        null=True, blank=True, related_name='message')
    email = models.EmailField(max_length=254, blank=False)
    email_subscription = models.BooleanField(default=False)
    message = models.TextField(blank=False)
    created_date = models.DateField(auto_now_add=True)

    class Meta:
        ordering = ['-created_date']

    def __str__(self):
        return self.name
