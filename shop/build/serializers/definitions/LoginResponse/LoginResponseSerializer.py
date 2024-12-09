from rest_framework import serializers

from dsu.dsu_gen.openapi.decorator.deserialize import deserialize
from dsu.dsu_gen.openapi.utils.type_file_utils import get_type_object
from dsu.dsu_gen.openapi.utils.type_file_utils import get_type_list_object
from dsu.dsu_gen.openapi.fields.collection_format_field import CollectionFormatField


class LoginResponseType(object):
    def __init__(self, token=None, user=None,  **kwargs):
        self.token = token
        self.user = user

    def __str__(self):
        from dsu.dsu_gen.openapi.utils.get_unicode_str import get_unicode_str
        return get_unicode_str(self).encode('utf-8')

    def __getitem__(self, item):
        return getattr(self, item)


class LoginResponseSerializer(serializers.Serializer):
    token = serializers.CharField(required=False, allow_blank=True, allow_null=True, help_text="The generated secure token for authentication.")
    from shop.build.serializers.definitions.LoginResponse.user.userSerializer import userSerializer
    user = userSerializer(required=False, allow_null=True)

    def create(self, validated_data):
        from shop.build.serializers.definitions.LoginResponse.user.userSerializer import userSerializer
        user_val, _ = deserialize(userSerializer, validated_data.pop("user", None), many=False, partial=True)
        
        return LoginResponseType(user=user_val, **validated_data)
