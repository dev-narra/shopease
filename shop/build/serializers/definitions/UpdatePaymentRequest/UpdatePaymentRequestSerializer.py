from rest_framework import serializers

from dsu.dsu_gen.openapi.decorator.deserialize import deserialize
from dsu.dsu_gen.openapi.utils.type_file_utils import get_type_object
from dsu.dsu_gen.openapi.utils.type_file_utils import get_type_list_object
from dsu.dsu_gen.openapi.fields.collection_format_field import CollectionFormatField


class UpdatePaymentRequestType(object):
    def __init__(self, amount, method, transaction_date,  **kwargs):
        self.amount = amount
        self.method = method
        self.transaction_date = transaction_date

    def __str__(self):
        from dsu.dsu_gen.openapi.utils.get_unicode_str import get_unicode_str
        return get_unicode_str(self).encode('utf-8')

    def __getitem__(self, item):
        return getattr(self, item)


class UpdatePaymentRequestSerializer(serializers.Serializer):
    amount = serializers.FloatField()
    method = serializers.CharField()
    transaction_date = serializers.CharField()

    def create(self, validated_data):
        return UpdatePaymentRequestType(**validated_data)
