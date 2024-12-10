from rest_framework import serializers

from dsu.dsu_gen.openapi.decorator.deserialize import deserialize
from dsu.dsu_gen.openapi.utils.type_file_utils import get_type_object
from dsu.dsu_gen.openapi.utils.type_file_utils import get_type_list_object
from dsu.dsu_gen.openapi.fields.collection_format_field import CollectionFormatField


class GetProductsRequestQueryParamType(object):
    def __init__(self, limit, offset,  **kwargs):
        self.limit = limit
        self.offset = offset

    def __str__(self):
        from dsu.dsu_gen.openapi.utils.get_unicode_str import get_unicode_str
        return get_unicode_str(self).encode('utf-8')

    def __getitem__(self, item):
        return getattr(self, item)


class GetProductsRequestQueryParamSerializer(serializers.Serializer):
    limit = serializers.IntegerField(help_text="The number of results per page for paginated results.", min_value=1, )
    offset = serializers.IntegerField(help_text="The starting point of the page of results to retrieve (e.g., offset = page_number * limit).", min_value=0, )

    def create(self, validated_data):
        return GetProductsRequestQueryParamType(**validated_data)
