from rest_framework import serializers
from shop.build.serializers.definitions.Customer.CustomerSerializer import CustomerSerializer

class Status_200Serializer(serializers.ListSerializer):
    child = CustomerSerializer()
