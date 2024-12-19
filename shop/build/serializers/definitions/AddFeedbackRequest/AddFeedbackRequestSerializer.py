from rest_framework import serializers

from dsu.dsu_gen.openapi.decorator.deserialize import deserialize
from dsu.dsu_gen.openapi.utils.type_file_utils import get_type_object
from dsu.dsu_gen.openapi.utils.type_file_utils import get_type_list_object
from dsu.dsu_gen.openapi.fields.collection_format_field import CollectionFormatField


class AddFeedbackRequestType(object):
    def __init__(self, rating, customer_id=None, review=None,  **kwargs):
        self.rating = rating
        self.customer_id = customer_id
        self.review = review

    def __str__(self):
        from dsu.dsu_gen.openapi.utils.get_unicode_str import get_unicode_str
        return get_unicode_str(self).encode('utf-8')

    def __getitem__(self, item):
        return getattr(self, item)


class AddFeedbackRequestSerializer(serializers.Serializer):
    customer_id = serializers.IntegerField(required=False, allow_null=True)
    rating = serializers.FloatField(help_text="The rating for the product, ranging from 1 to 5.", max_value=5.000000, min_value=1.000000)
    review = serializers.CharField(required=False, allow_blank=True, allow_null=True, help_text="The written review for the product.")

    def create(self, validated_data):
        return AddFeedbackRequestType(**validated_data)
