from rest_framework import serializers

from dsu.dsu_gen.openapi.decorator.deserialize import deserialize
from dsu.dsu_gen.openapi.utils.type_file_utils import get_type_object
from dsu.dsu_gen.openapi.utils.type_file_utils import get_type_list_object
from dsu.dsu_gen.openapi.fields.collection_format_field import CollectionFormatField


class SearchCustomersRequestQueryParamType(object):
    def __init__(self, name=None, email=None,  **kwargs):
        self.name = name
        self.email = email

    def __str__(self):
        from dsu.dsu_gen.openapi.utils.get_unicode_str import get_unicode_str
        return get_unicode_str(self).encode('utf-8')

    def __getitem__(self, item):
        return getattr(self, item)


class SearchCustomersRequestQueryParamSerializer(serializers.Serializer):
    name = serializers.CharField(required=False, allow_blank=True, allow_null=True, help_text="The name of the customer to search for.")
    email = serializers.CharField(required=False, allow_blank=True, allow_null=True, help_text="The email of the customer to search for.")

    def create(self, validated_data):
        return SearchCustomersRequestQueryParamType(**validated_data)
