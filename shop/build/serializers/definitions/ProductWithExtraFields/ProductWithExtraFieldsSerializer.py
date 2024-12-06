from shop.build.serializers.definitions.Product.ProductSerializer import ProductSerializer
from shop.build.serializers.definitions.Product.ProductSerializer import ProductType
from shop.build.serializers.definitions.ProductWithExtraFields.ProductWithExtraFields.Schema1.Schema1Serializer import Schema1Serializer
from shop.build.serializers.definitions.ProductWithExtraFields.ProductWithExtraFields.Schema1.Schema1Serializer import Schema1Type

from dsu.dsu_gen.openapi.decorator.deserialize import deserialize

class ProductWithExtraFieldsType(ProductType, Schema1Type):
    def __init__(self, **validated_data):
        ProductType.__init__(self, **validated_data)
        Schema1Type.__init__(self, **validated_data)
        

class ProductWithExtraFieldsSerializer(ProductSerializer, Schema1Serializer):
    def create(self, validated_data):
        
        productSerializer, _ = deserialize(ProductSerializer, validated_data, many=False, partial=True)
        validated_data.update(productSerializer.__dict__)
        
        schema1Serializer, _ = deserialize(Schema1Serializer, validated_data, many=False, partial=True)
        validated_data.update(schema1Serializer.__dict__)
        
        return ProductWithExtraFieldsType(**validated_data)
