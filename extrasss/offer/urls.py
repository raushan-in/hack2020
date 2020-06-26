from django.urls import path
from offer.views import ActiveOffers #, OfferStats

urlpatterns = [
    path('active/', ActiveOffers.as_view(),name='offer-active'),
    # path('stats/', OfferStats.as_view(),name='offer-stats'),
]