from rest_framework import serializers

from dsu.dsu_gen.openapi.decorator.deserialize import deserialize
from dsu.dsu_gen.openapi.utils.type_file_utils import get_type_object
from dsu.dsu_gen.openapi.utils.type_file_utils import get_type_list_object
from dsu.dsu_gen.openapi.fields.collection_format_field import CollectionFormatField


class UpdateFeedbackRequestType(object):
    def __init__(self, rating, review,  **kwargs):
        self.rating = rating
        self.review = review

    def __str__(self):
        from dsu.dsu_gen.openapi.utils.get_unicode_str import get_unicode_str
        return get_unicode_str(self).encode('utf-8')

    def __getitem__(self, item):
        return getattr(self, item)


class UpdateFeedbackRequestSerializer(serializers.Serializer):
    rating = serializers.FloatField(help_text="The new rating for the product, a number between 1 and 5.", max_value=5.000000, min_value=1.000000)
    review = serializers.CharField(help_text="The new review text for the product.")

    def create(self, validated_data):
        return UpdateFeedbackRequestType(**validated_data)
