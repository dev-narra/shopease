from shop.build.serializers.definitions.Customer.CustomerSerializer import CustomerSerializer
from shop.build.serializers.definitions.Customer.CustomerSerializer import CustomerType
from shop.build.serializers.definitions.CustomerWithExtraFields.CustomerWithExtraFields.Schema1.Schema1Serializer import Schema1Serializer
from shop.build.serializers.definitions.CustomerWithExtraFields.CustomerWithExtraFields.Schema1.Schema1Serializer import Schema1Type

from dsu.dsu_gen.openapi.decorator.deserialize import deserialize

class CustomerWithExtraFieldsType(CustomerType, Schema1Type):
    def __init__(self, **validated_data):
        CustomerType.__init__(self, **validated_data)
        Schema1Type.__init__(self, **validated_data)
        

class CustomerWithExtraFieldsSerializer(CustomerSerializer, Schema1Serializer):
    def create(self, validated_data):
        
        customerSerializer, _ = deserialize(CustomerSerializer, validated_data, many=False, partial=True)
        validated_data.update(customerSerializer.__dict__)
        
        schema1Serializer, _ = deserialize(Schema1Serializer, validated_data, many=False, partial=True)
        validated_data.update(schema1Serializer.__dict__)
        
        return CustomerWithExtraFieldsType(**validated_data)
