from rest_framework import serializers

from dsu.dsu_gen.openapi.decorator.deserialize import deserialize
from dsu.dsu_gen.openapi.utils.type_file_utils import get_type_object
from dsu.dsu_gen.openapi.utils.type_file_utils import get_type_list_object
from dsu.dsu_gen.openapi.fields.collection_format_field import CollectionFormatField


class Status_200Type(object):
    def __init__(self, message=None, orderId=None, status=None,  **kwargs):
        self.message = message
        self.orderId = orderId
        self.status = status

    def __str__(self):
        from dsu.dsu_gen.openapi.utils.get_unicode_str import get_unicode_str
        return get_unicode_str(self).encode('utf-8')

    def __getitem__(self, item):
        return getattr(self, item)


class Status_200Serializer(serializers.Serializer):
    message = serializers.CharField(required=False, allow_blank=True, allow_null=True)
    orderId = serializers.IntegerField(required=False, allow_null=True)
    status = serializers.CharField(required=False, allow_blank=True, allow_null=True)

    def create(self, validated_data):
        return Status_200Type(**validated_data)
