from rest_framework import serializers

from dsu.dsu_gen.openapi.decorator.deserialize import deserialize
from dsu.dsu_gen.openapi.utils.type_file_utils import get_type_object
from dsu.dsu_gen.openapi.utils.type_file_utils import get_type_list_object
from dsu.dsu_gen.openapi.fields.collection_format_field import CollectionFormatField


class ListOrdersRequestQueryParamType(object):
    def __init__(self, page=None, size=None,  **kwargs):
        self.page = page
        self.size = size

    def __str__(self):
        from dsu.dsu_gen.openapi.utils.get_unicode_str import get_unicode_str
        return get_unicode_str(self).encode('utf-8')

    def __getitem__(self, item):
        return getattr(self, item)


class ListOrdersRequestQueryParamSerializer(serializers.Serializer):
    page = serializers.IntegerField(required=False, allow_null=True, help_text="The page number to retrieve.", min_value=1, )
    size = serializers.IntegerField(required=False, allow_null=True, help_text="The number of orders per page.", min_value=1, )

    def create(self, validated_data):
        return ListOrdersRequestQueryParamType(**validated_data)
