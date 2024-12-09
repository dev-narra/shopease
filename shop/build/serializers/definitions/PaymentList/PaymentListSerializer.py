from rest_framework import serializers

from dsu.dsu_gen.openapi.decorator.deserialize import deserialize
from dsu.dsu_gen.openapi.utils.type_file_utils import get_type_object
from dsu.dsu_gen.openapi.utils.type_file_utils import get_type_list_object
from dsu.dsu_gen.openapi.fields.collection_format_field import CollectionFormatField


class PaymentListType(object):
    def __init__(self, payments=None, total=None, page=None, size=None,  **kwargs):
        self.payments = payments
        self.total = total
        self.page = page
        self.size = size

    def __str__(self):
        from dsu.dsu_gen.openapi.utils.get_unicode_str import get_unicode_str
        return get_unicode_str(self).encode('utf-8')

    def __getitem__(self, item):
        return getattr(self, item)


class PaymentListSerializer(serializers.Serializer):
    from shop.build.serializers.definitions.Payment.PaymentSerializer import PaymentSerializer
    payments = PaymentSerializer(required=False, many=True)
    total = serializers.IntegerField(required=False, allow_null=True)
    page = serializers.IntegerField(required=False, allow_null=True)
    size = serializers.IntegerField(required=False, allow_null=True)

    def create(self, validated_data):
        from shop.build.serializers.definitions.Payment.PaymentSerializer import PaymentSerializer
        payments_val = []
        payments_list_val = validated_data.pop("payments", [])
        for each_data in payments_list_val:
            each_obj, _ = deserialize(PaymentSerializer, each_data, many=False, partial=True)
            payments_val.append(each_obj)
        
        return PaymentListType(payments=payments_val, **validated_data)
