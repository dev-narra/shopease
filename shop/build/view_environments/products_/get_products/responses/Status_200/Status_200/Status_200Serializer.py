from rest_framework import serializers
from shop.build.serializers.definitions.Product.ProductSerializer import ProductSerializer

class Status_200Serializer(serializers.ListSerializer):
    child = ProductSerializer()
