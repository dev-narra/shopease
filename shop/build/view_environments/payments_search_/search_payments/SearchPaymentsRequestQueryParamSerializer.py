from rest_framework import serializers

from dsu.dsu_gen.openapi.decorator.deserialize import deserialize
from dsu.dsu_gen.openapi.utils.type_file_utils import get_type_object
from dsu.dsu_gen.openapi.utils.type_file_utils import get_type_list_object
from dsu.dsu_gen.openapi.fields.collection_format_field import CollectionFormatField


class SearchPaymentsRequestQueryParamType(object):
    def __init__(self, orderId=None, customerName=None,  **kwargs):
        self.orderId = orderId
        self.customerName = customerName

    def __str__(self):
        from dsu.dsu_gen.openapi.utils.get_unicode_str import get_unicode_str
        return get_unicode_str(self).encode('utf-8')

    def __getitem__(self, item):
        return getattr(self, item)


class SearchPaymentsRequestQueryParamSerializer(serializers.Serializer):
    orderId = serializers.IntegerField(required=False, allow_null=True, help_text="The ID of the order to filter payments.")
    customerName = serializers.CharField(required=False, allow_blank=True, allow_null=True, help_text="The name of the customer to filter payments.")

    def create(self, validated_data):
        return SearchPaymentsRequestQueryParamType(**validated_data)
