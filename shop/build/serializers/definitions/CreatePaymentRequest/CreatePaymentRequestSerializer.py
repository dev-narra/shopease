from rest_framework import serializers

from dsu.dsu_gen.openapi.decorator.deserialize import deserialize
from dsu.dsu_gen.openapi.utils.type_file_utils import get_type_object
from dsu.dsu_gen.openapi.utils.type_file_utils import get_type_list_object
from dsu.dsu_gen.openapi.fields.collection_format_field import CollectionFormatField


class CreatePaymentRequestType(object):
    def __init__(self, amount, method,  **kwargs):
        self.amount = amount
        self.method = method

    def __str__(self):
        from dsu.dsu_gen.openapi.utils.get_unicode_str import get_unicode_str
        return get_unicode_str(self).encode('utf-8')

    def __getitem__(self, item):
        return getattr(self, item)


class CreatePaymentRequestSerializer(serializers.Serializer):
    amount = serializers.FloatField(help_text="The payment amount for the order.")
    method = serializers.ChoiceField(choices=(('Credit Card', 'Credit Card'), ('Debit Card', 'Debit Card'), ('PayPal', 'PayPal'), ('Bank Transfer', 'Bank Transfer')), help_text="The method of payment.")

    def create(self, validated_data):
        return CreatePaymentRequestType(**validated_data)
