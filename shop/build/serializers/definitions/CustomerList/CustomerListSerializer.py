from rest_framework import serializers

from dsu.dsu_gen.openapi.decorator.deserialize import deserialize
from dsu.dsu_gen.openapi.utils.type_file_utils import get_type_object
from dsu.dsu_gen.openapi.utils.type_file_utils import get_type_list_object
from dsu.dsu_gen.openapi.fields.collection_format_field import CollectionFormatField


class CustomerListType(object):
    def __init__(self, customers=None, total=None, page=None, size=None,  **kwargs):
        self.customers = customers
        self.total = total
        self.page = page
        self.size = size

    def __str__(self):
        from dsu.dsu_gen.openapi.utils.get_unicode_str import get_unicode_str
        return get_unicode_str(self).encode('utf-8')

    def __getitem__(self, item):
        return getattr(self, item)


class CustomerListSerializer(serializers.Serializer):
    from shop.build.serializers.definitions.Customer.CustomerSerializer import CustomerSerializer
    customers = CustomerSerializer(required=False, many=True)
    total = serializers.IntegerField(required=False, allow_null=True)
    page = serializers.IntegerField(required=False, allow_null=True)
    size = serializers.IntegerField(required=False, allow_null=True)

    def create(self, validated_data):
        from shop.build.serializers.definitions.Customer.CustomerSerializer import CustomerSerializer
        customers_val = []
        customers_list_val = validated_data.pop("customers", [])
        for each_data in customers_list_val:
            each_obj, _ = deserialize(CustomerSerializer, each_data, many=False, partial=True)
            customers_val.append(each_obj)
        
        return CustomerListType(customers=customers_val, **validated_data)
