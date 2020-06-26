from django.db import models
from . import *
from offer.models import Offers
from offer.utils import get_code, get_expiry
from django.db import transaction
from django.utils.functional import cached_property

class Partners(models.Model):  
    name = models.CharField(max_length=50, unique=True)
    gst = models.CharField(max_length = 150, null=True, blank=True)
    logo = models.ImageField(upload_to='partner_photo/', default='partner_photo/default.jpg')
    info = models.TextField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'Partners'

    def __str__(self):
        return f'{self.name}'

class Vouchers(models.Model):  
    code = models.CharField(max_length=32, unique=True)
    partner = models.ForeignKey(Partners, null=True, blank=True,
                                on_delete=models.SET_NULL, related_name="partner")
    offer = models.ForeignKey(Offers, on_delete=models.CASCADE, related_name="offer")
    quantity = models.SmallIntegerField(default=1)
    availed_count = models.SmallIntegerField(default=0)
    email = models.EmailField()
    mobile = models.CharField(max_length=15, blank=True, null=True)
    expiry = models.DateTimeField(auto_now=False, auto_now_add=False)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'Vouchers'

    def __str__(self):
        return f'{self.code}'

    @transaction.atomic
    def generate_voucher(self, serializer):
        email = serializer.validated_data['user_email']
        offer = serializer.validated_data['itilite_offer_id']
        self.email = email
        self.offer = offer
        self.code = get_code(email)
        self.expiry = get_expiry(offer.validity)
        self.partner = serializer.validated_data['platform']
        self.quantity = serializer.validated_data['quantity']
        self.mobile = serializer.validated_data.get('user_mobile',None)
        self.save()
        return self

    @cached_property
    def usability(self):
        return self.offer.own_use_only

    