from rest_framework import serializers

from dsu.dsu_gen.openapi.decorator.deserialize import deserialize
from dsu.dsu_gen.openapi.utils.type_file_utils import get_type_object
from dsu.dsu_gen.openapi.utils.type_file_utils import get_type_list_object
from dsu.dsu_gen.openapi.fields.collection_format_field import CollectionFormatField


class userType(object):
    def __init__(self, id=None, email=None, role=None,  **kwargs):
        self.id = id
        self.email = email
        self.role = role

    def __str__(self):
        from dsu.dsu_gen.openapi.utils.get_unicode_str import get_unicode_str
        return get_unicode_str(self).encode('utf-8')

    def __getitem__(self, item):
        return getattr(self, item)


class userSerializer(serializers.Serializer):
    id = serializers.IntegerField(required=False, allow_null=True, help_text="The unique ID of the user.")
    email = serializers.EmailField(required=False, allow_blank=True, allow_null=True, help_text="The email address of the user.")
    role = serializers.CharField(required=False, allow_blank=True, allow_null=True, help_text="The role of the user (Admin or Customer).")

    def create(self, validated_data):
        return userType(**validated_data)
