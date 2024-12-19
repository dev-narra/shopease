from rest_framework import serializers
from shop.build.serializers.definitions.Feedback.FeedbackSerializer import FeedbackSerializer

class Status_200Serializer(serializers.ListSerializer):
    child = FeedbackSerializer()
