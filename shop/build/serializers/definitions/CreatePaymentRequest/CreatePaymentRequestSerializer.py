from rest_framework import serializers

from dsu.dsu_gen.openapi.decorator.deserialize import deserialize
from dsu.dsu_gen.openapi.utils.type_file_utils import get_type_object
from dsu.dsu_gen.openapi.utils.type_file_utils import get_type_list_object
from dsu.dsu_gen.openapi.fields.collection_format_field import CollectionFormatField


class CreatePaymentRequestType(object):
    def __init__(self, orderId, amount, paymentMethod, paymentDate=None,  **kwargs):
        self.orderId = orderId
        self.amount = amount
        self.paymentMethod = paymentMethod
        self.paymentDate = paymentDate

    def __str__(self):
        from dsu.dsu_gen.openapi.utils.get_unicode_str import get_unicode_str
        return get_unicode_str(self).encode('utf-8')

    def __getitem__(self, item):
        return getattr(self, item)


class CreatePaymentRequestSerializer(serializers.Serializer):
    orderId = serializers.IntegerField(help_text="The unique ID of the order for which the payment is being made.")
    amount = serializers.FloatField(help_text="The payment amount for the order.")
    paymentMethod = serializers.ChoiceField(choices=(('Credit Card', 'Credit Card'), ('Debit Card', 'Debit Card'), ('PayPal', 'PayPal'), ('Bank Transfer', 'Bank Transfer')), help_text="The method of payment.")
    paymentDate = serializers.DateTimeField(required=False, allow_null=True, help_text="The date and time when the payment was made.", format='%Y-%m-%d %H:%M:%S')

    def create(self, validated_data):
        return CreatePaymentRequestType(**validated_data)
