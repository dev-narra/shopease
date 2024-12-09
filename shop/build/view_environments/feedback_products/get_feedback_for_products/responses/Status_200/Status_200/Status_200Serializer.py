from rest_framework import serializers

from dsu.dsu_gen.openapi.decorator.deserialize import deserialize
from dsu.dsu_gen.openapi.utils.type_file_utils import get_type_object
from dsu.dsu_gen.openapi.utils.type_file_utils import get_type_list_object
from dsu.dsu_gen.openapi.fields.collection_format_field import CollectionFormatField


class Status_200Type(object):
    def __init__(self, page=None, size=None, totalPages=None, totalFeedback=None, feedback=None,  **kwargs):
        self.page = page
        self.size = size
        self.totalPages = totalPages
        self.totalFeedback = totalFeedback
        self.feedback = feedback

    def __str__(self):
        from dsu.dsu_gen.openapi.utils.get_unicode_str import get_unicode_str
        return get_unicode_str(self).encode('utf-8')

    def __getitem__(self, item):
        return getattr(self, item)


class Status_200Serializer(serializers.Serializer):
    page = serializers.IntegerField(required=False, allow_null=True)
    size = serializers.IntegerField(required=False, allow_null=True)
    totalPages = serializers.IntegerField(required=False, allow_null=True)
    totalFeedback = serializers.IntegerField(required=False, allow_null=True)
    from shop.build.serializers.definitions.Feedback.FeedbackSerializer import FeedbackSerializer
    feedback = FeedbackSerializer(required=False, many=True)

    def create(self, validated_data):
        from shop.build.serializers.definitions.Feedback.FeedbackSerializer import FeedbackSerializer
        feedback_val = []
        feedback_list_val = validated_data.pop("feedback", [])
        for each_data in feedback_list_val:
            each_obj, _ = deserialize(FeedbackSerializer, each_data, many=False, partial=True)
            feedback_val.append(each_obj)
        
        return Status_200Type(feedback=feedback_val, **validated_data)
