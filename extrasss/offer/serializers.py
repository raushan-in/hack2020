from rest_framework import serializers
from .models import Offers


class OfferListSerializer(serializers.ModelSerializer):
    currency = serializers.CharField(source='get_currency_display')

    class Meta:
        model = Offers
        fields = (
                'id', 'name', 'image', 'active', 'price', 'currency', 'validity', 'tag',
                'description', 'terms', 'guide' 
            )