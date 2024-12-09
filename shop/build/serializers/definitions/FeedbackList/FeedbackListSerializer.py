from rest_framework import serializers

from dsu.dsu_gen.openapi.decorator.deserialize import deserialize
from dsu.dsu_gen.openapi.utils.type_file_utils import get_type_object
from dsu.dsu_gen.openapi.utils.type_file_utils import get_type_list_object
from dsu.dsu_gen.openapi.fields.collection_format_field import CollectionFormatField


class FeedbackListType(object):
    def __init__(self, total=None, limit=None, offset=None, feedback=None,  **kwargs):
        self.total = total
        self.limit = limit
        self.offset = offset
        self.feedback = feedback

    def __str__(self):
        from dsu.dsu_gen.openapi.utils.get_unicode_str import get_unicode_str
        return get_unicode_str(self).encode('utf-8')

    def __getitem__(self, item):
        return getattr(self, item)


class FeedbackListSerializer(serializers.Serializer):
    total = serializers.IntegerField(required=False, allow_null=True)
    limit = serializers.IntegerField(required=False, allow_null=True)
    offset = serializers.IntegerField(required=False, allow_null=True)
    from shop.build.serializers.definitions.Feedback.FeedbackSerializer import FeedbackSerializer
    feedback = FeedbackSerializer(required=False, many=True)

    def create(self, validated_data):
        from shop.build.serializers.definitions.Feedback.FeedbackSerializer import FeedbackSerializer
        feedback_val = []
        feedback_list_val = validated_data.pop("feedback", [])
        for each_data in feedback_list_val:
            each_obj, _ = deserialize(FeedbackSerializer, each_data, many=False, partial=True)
            feedback_val.append(each_obj)
        
        return FeedbackListType(feedback=feedback_val, **validated_data)
