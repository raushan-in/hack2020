from django.urls import path
from voucher.views import  GenerateVoucher #, AvailVoucher

urlpatterns = [
    # path('avail/', AvailVoucher.as_view(),name='voucher-avail'),
    path('generate/', GenerateVoucher.as_view(),name='voucher-generate'),
]