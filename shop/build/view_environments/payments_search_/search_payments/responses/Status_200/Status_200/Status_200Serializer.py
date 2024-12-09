from rest_framework import serializers
from shop.build.serializers.definitions.Payment.PaymentSerializer import PaymentSerializer

class Status_200Serializer(serializers.ListSerializer):
    child = PaymentSerializer()
