from rest_framework import serializers

from dsu.dsu_gen.openapi.decorator.deserialize import deserialize
from dsu.dsu_gen.openapi.utils.type_file_utils import get_type_object
from dsu.dsu_gen.openapi.utils.type_file_utils import get_type_list_object
from dsu.dsu_gen.openapi.fields.collection_format_field import CollectionFormatField


class AddProductFeedbackRequestPathParamType(object):
    def __init__(self, productId,  **kwargs):
        self.productId = productId

    def __str__(self):
        from dsu.dsu_gen.openapi.utils.get_unicode_str import get_unicode_str
        return get_unicode_str(self).encode('utf-8')

    def __getitem__(self, item):
        return getattr(self, item)


class AddProductFeedbackRequestPathParamSerializer(serializers.Serializer):
    productId = serializers.IntegerField(help_text="The unique ID of the product for which feedback is being submitted.")

    def create(self, validated_data):
        return AddProductFeedbackRequestPathParamType(**validated_data)
