from rest_framework import serializers

from dsu.dsu_gen.openapi.decorator.deserialize import deserialize
from dsu.dsu_gen.openapi.utils.type_file_utils import get_type_object
from dsu.dsu_gen.openapi.utils.type_file_utils import get_type_list_object
from dsu.dsu_gen.openapi.fields.collection_format_field import CollectionFormatField


class SearchOrdersRequestQueryParamType(object):
    def __init__(self, customer=None, status=None,  **kwargs):
        self.customer = customer
        self.status = status

    def __str__(self):
        from dsu.dsu_gen.openapi.utils.get_unicode_str import get_unicode_str
        return get_unicode_str(self).encode('utf-8')

    def __getitem__(self, item):
        return getattr(self, item)


class SearchOrdersRequestQueryParamSerializer(serializers.Serializer):
    customer = serializers.CharField(required=False, allow_blank=True, allow_null=True, help_text="The name of the customer to search for orders.")
    status = serializers.CharField(required=False, allow_blank=True, allow_null=True, help_text="The status of the order to search (e.g., Pending, Shipped, Delivered).")

    def create(self, validated_data):
        return SearchOrdersRequestQueryParamType(**validated_data)
