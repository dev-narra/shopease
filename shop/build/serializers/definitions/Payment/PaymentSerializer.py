from rest_framework import serializers

from dsu.dsu_gen.openapi.decorator.deserialize import deserialize
from dsu.dsu_gen.openapi.utils.type_file_utils import get_type_object
from dsu.dsu_gen.openapi.utils.type_file_utils import get_type_list_object
from dsu.dsu_gen.openapi.fields.collection_format_field import CollectionFormatField


class PaymentType(object):
    def __init__(self, id=None, order_id=None, amount=None, method=None, status=None, transaction_date=None,  **kwargs):
        self.id = id
        self.order_id = order_id
        self.amount = amount
        self.method = method
        self.status = status
        self.transaction_date = transaction_date

    def __str__(self):
        from dsu.dsu_gen.openapi.utils.get_unicode_str import get_unicode_str
        return get_unicode_str(self).encode('utf-8')

    def __getitem__(self, item):
        return getattr(self, item)


class PaymentSerializer(serializers.Serializer):
    id = serializers.CharField(required=False, allow_blank=True, allow_null=True)
    order_id = serializers.CharField(required=False, allow_blank=True, allow_null=True)
    amount = serializers.FloatField(required=False, allow_null=True)
    method = serializers.ChoiceField(choices=(('Card', 'Card'), ('NetBanking', 'NetBanking'), ('UPI', 'UPI'), ('COD', 'COD')), required=False, allow_blank=True, allow_null=True)
    status = serializers.ChoiceField(choices=(('Success', 'Success'), ('Pending', 'Pending'), ('Failed', 'Failed')), required=False, allow_blank=True, allow_null=True)
    transaction_date = serializers.DateTimeField(required=False, allow_null=True, format='%Y-%m-%d %H:%M:%S')

    def create(self, validated_data):
        return PaymentType(**validated_data)