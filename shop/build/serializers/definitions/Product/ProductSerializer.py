from shop.build.serializers.definitions.BasicProduct.BasicProductSerializer import BasicProductSerializer
from shop.build.serializers.definitions.BasicProduct.BasicProductSerializer import BasicProductType
from shop.build.serializers.definitions.ProductId.ProductIdSerializer import ProductIdSerializer
from shop.build.serializers.definitions.ProductId.ProductIdSerializer import ProductIdType

from dsu.dsu_gen.openapi.decorator.deserialize import deserialize

class ProductType(BasicProductType, ProductIdType):
    def __init__(self, **validated_data):
        BasicProductType.__init__(self, **validated_data)
        ProductIdType.__init__(self, **validated_data)
        

class ProductSerializer(BasicProductSerializer, ProductIdSerializer):
    def create(self, validated_data):
        
        basicProductSerializer, _ = deserialize(BasicProductSerializer, validated_data, many=False, partial=True)
        validated_data.update(basicProductSerializer.__dict__)
        
        productIdSerializer, _ = deserialize(ProductIdSerializer, validated_data, many=False, partial=True)
        validated_data.update(productIdSerializer.__dict__)
        
        return ProductType(**validated_data)
