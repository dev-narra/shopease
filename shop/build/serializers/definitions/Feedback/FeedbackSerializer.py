from rest_framework import serializers

from dsu.dsu_gen.openapi.decorator.deserialize import deserialize
from dsu.dsu_gen.openapi.utils.type_file_utils import get_type_object
from dsu.dsu_gen.openapi.utils.type_file_utils import get_type_list_object
from dsu.dsu_gen.openapi.fields.collection_format_field import CollectionFormatField


class FeedbackType(object):
    def __init__(self, rating, review=None,  **kwargs):
        self.rating = rating
        self.review = review

    def __str__(self):
        from dsu.dsu_gen.openapi.utils.get_unicode_str import get_unicode_str
        return get_unicode_str(self).encode('utf-8')

    def __getitem__(self, item):
        return getattr(self, item)


class FeedbackSerializer(serializers.Serializer):
    rating = serializers.FloatField(max_value=5.000000, min_value=1.000000)
    review = serializers.CharField(required=False, allow_blank=True, allow_null=True)

    def create(self, validated_data):
        return FeedbackType(**validated_data)
