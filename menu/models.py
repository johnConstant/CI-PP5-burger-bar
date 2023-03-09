from django.db import models
from cloudinary.models import CloudinaryField


STATUS = ((0, 'Draft'), (1, 'Published'))


class Allergen(models.Model):
    """
    A class for the Allergens model
    """
    name = models.CharField(max_length=256, unique=True)
    icon = CloudinaryField('image', default='placeholder')
    description = models.TextField()

    def __str__(self):
        return self.name


class Menu_Category(models.Model):
    """
    A class for the Menu Category model
    """
    class Meta:
        verbose_name_plural = 'Menu Categories'

    name = models.CharField(max_length=256, unique=True)
    slug = models.SlugField(max_length=256, unique=True, null=True)
    featured_image = CloudinaryField('image', default='placeholder')
    description = models.TextField()

    def __str__(self):
        return self.name


class Menu_Item(models.Model):
    """
    A class for the Menu Item model
    """
    class Meta:
        verbose_name_plural = 'Menu Items'

    name = models.CharField(max_length=256, unique=True)
    slug = models.SlugField(max_length=256, unique=True, null=True)
    description = models.TextField()
    price = models.DecimalField(max_digits=4, decimal_places=2)
    featured_image = CloudinaryField('image', default='placeholder')
    allergens = models.ManyToManyField(
        Allergen, related_name='allergen', blank=True
        )
    category = models.ForeignKey(
        'Menu_Category', null=True, blank=True, related_name="items",
        on_delete=models.SET_NULL
        )
    status = models.IntegerField(choices=STATUS, default=0)
    featured = models.BooleanField(default=False)

    def __str__(self):
        return self.name
