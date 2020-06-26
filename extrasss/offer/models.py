from django.db import models
from offer.utils import ListField
from . import *

class Offers(models.Model):  
    name = models.CharField(max_length=50, unique=True)
    image = models.ImageField(upload_to='offer_photo/', default='offer_photo/default.jpg')
    price = models.DecimalField(max_digits=8, decimal_places=2)
    currency = models.SmallIntegerField(choices=CURRENCY_CHOICES, default=INR)
    validity = models.PositiveSmallIntegerField() # in months
    tag = models.TextField()
    description = models.TextField()
    terms = ListField()
    guide = ListField()
    own_use_only = models.BooleanField(default=False)
    active = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'Offers'

    def __str__(self):
        return f'{self.name}'
