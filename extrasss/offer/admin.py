from django.contrib import admin
from .models import Offers


class OfferAdmin(admin.ModelAdmin):
    list_display = ('name', 'active', 'own_use_only')

admin.site.register(Offers, OfferAdmin)
