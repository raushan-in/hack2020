from django.shortcuts import render
from django.shortcuts import render
from rest_framework import exceptions, generics, permissions, response, status
from .serializers import CreateVoucherSerializer, VoucherSerializer
from .models import Vouchers

class GenerateVoucher(generics.CreateAPIView):
    serializer_class = CreateVoucherSerializer

    def perform_create(self, serializer):
        kwargs = {
            "first_team_id": serializer.validated_data['first_team'],
            "second_team_id": serializer.validated_data['second_team']
        }
        # return Match().create_match(**kwargs)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        instance = Vouchers().generate_voucher(serializer)
        instance_serializer = VoucherSerializer(instance)  # response serializer
        return response.Response(instance_serializer.data)
