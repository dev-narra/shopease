from rest_framework import serializers

from dsu.dsu_gen.openapi.decorator.deserialize import deserialize
from dsu.dsu_gen.openapi.utils.type_file_utils import get_type_object
from dsu.dsu_gen.openapi.utils.type_file_utils import get_type_list_object
from dsu.dsu_gen.openapi.fields.collection_format_field import CollectionFormatField


class CustomerIdType(object):
    def __init__(self, customer_id=None,  **kwargs):
        self.customer_id = customer_id

    def __str__(self):
        from dsu.dsu_gen.openapi.utils.get_unicode_str import get_unicode_str
        return get_unicode_str(self).encode('utf-8')

    def __getitem__(self, item):
        return getattr(self, item)


class CustomerIdSerializer(serializers.Serializer):
    customer_id = serializers.IntegerField(required=False, allow_null=True)

    def create(self, validated_data):
        return CustomerIdType(**validated_data)
