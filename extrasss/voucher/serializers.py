from rest_framework import serializers
from .models import Partners, Vouchers
from offer.models import Offers


class CreateVoucherSerializer(serializers.Serializer):
    user_email = serializers.EmailField()
    platform = serializers.CharField()
    amount = serializers.DecimalField(max_digits=8, decimal_places=2)
    quantity = serializers.IntegerField()
    itilite_offer_id = serializers.IntegerField()
    user_mobile = serializers.CharField(required=False)

    class Meta:
        fields = (
                'user_email', 'platform', 'amount', 'quantity', 'itilite_offer_id', 'user_mobile'
            )

    def validate_platform(self, value):
        try: 
            partner = Partners.objects.get(name__iexact=value)
            return partner
        except:
            raise serializers.ValidationError("Invalid partner platform. \n please contact support@itilite.com.")

    def validate_itilite_offer_id(self, value):
        try:
            offer = Offers.objects.get(pk=value, active=True)
            return offer
        except:
            raise serializers.ValidationError("Invalid offer id. \n please contact support@itilite.com.")
        
    def validate(self, data):
        offer= data['itilite_offer_id']
        quantity = data['quantity']
        amount = data['amount']

        expacted_amount = offer.price * quantity
        if expacted_amount != amount:
            raise serializers.ValidationError("Invalid quantity and amount. \n please contact support@itilite.com.")
        return data



class VoucherSerializer(serializers.ModelSerializer):
    use_limit = serializers.IntegerField(source='quantity')
    own_use_only = serializers.BooleanField(source='usability')
    expiry = serializers.DateTimeField()
    
    class Meta:
        model = Vouchers
        fields = (
                'pk', 'code', 'expiry', 'email', 'use_limit', 'own_use_only'
            )