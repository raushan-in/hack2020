from django.shortcuts import render
from rest_framework import generics, permissions, response, serializers
from offer.serializers import OfferListSerializer
from .models import Offers


class ActiveOffers(generics.ListAPIView):
    serializer_class = OfferListSerializer
    permission_classes = (permissions.AllowAny,)
    queryset = Offers.objects.filter(active=True)
    
