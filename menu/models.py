from django.db import models
from cloudinary.models import CloudinaryField

ALLERGENS = [
    ('None', 'none'),
    ('Peanut', 'peanut'),
    ('Dairy', 'dairy'),
    ('Eggs', 'eggs'),
    ('Fish', 'fish')
]


# Create your models here.
class Menu_Category(models.Model):

    class Meta:
        verbose_name_plural = 'Menu Categories'

    name = models.CharField(max_length=256, unique=True)
    slug = models.SlugField(max_length=256, unique=True, null=True)
    featured_image = CloudinaryField('image', default='placeholder')
    description = models.TextField()

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


class Menu_Item(models.Model):

    class Meta:
        verbose_name_plural = 'Menu Items'

    category = models.ForeignKey(
        'Menu_Category', null=True, blank=True, on_delete=models.SET_NULL
        )
    name = models.CharField(max_length=256, unique=True)
    slug = models.SlugField(max_length=256, unique=True, null=True)
    description = models.TextField()
    price = models.DecimalField(max_digits=4, decimal_places=2)
    featured_image = CloudinaryField('image', default='placeholder')
    allergens = models.CharField(
        choices=ALLERGENS,
        max_length=100,
        default='none'
        )

    def __str__(self):
        return self.name


class Special_Offer(models.Model):

    class Meta:
        verbose_name_plural = 'Special Offers'

    name = models.CharField(max_length=256, unique=True)
    slug = models.SlugField(max_length=256, unique=True, null=True)
    description = models.TextField()
    price = models.DecimalField(max_digits=4, decimal_places=2)
    items = models.ManyToManyField(
        Menu_Item, related_name='offer_item', blank=False
        )

    def __str__(self):
        return self.name
