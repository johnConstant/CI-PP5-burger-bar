from django.db import models

# Create your models here.


class FAQ(models.Model):

    class Meta:
        verbose_name_plural = 'FAQs'

    question = models.TextField()
    answer = models.TextField()

    def __str__(self):
        return self.question
