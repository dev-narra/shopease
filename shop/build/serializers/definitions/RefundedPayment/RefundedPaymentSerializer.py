from rest_framework import serializers

from dsu.dsu_gen.openapi.decorator.deserialize import deserialize
from dsu.dsu_gen.openapi.utils.type_file_utils import get_type_object
from dsu.dsu_gen.openapi.utils.type_file_utils import get_type_list_object
from dsu.dsu_gen.openapi.fields.collection_format_field import CollectionFormatField


class RefundedPaymentType(object):
    def __init__(self, paymentId=None, orderId=None, customerId=None, refundAmount=None, status=None, refundDate=None,  **kwargs):
        self.paymentId = paymentId
        self.orderId = orderId
        self.customerId = customerId
        self.refundAmount = refundAmount
        self.status = status
        self.refundDate = refundDate

    def __str__(self):
        from dsu.dsu_gen.openapi.utils.get_unicode_str import get_unicode_str
        return get_unicode_str(self).encode('utf-8')

    def __getitem__(self, item):
        return getattr(self, item)


class RefundedPaymentSerializer(serializers.Serializer):
    paymentId = serializers.IntegerField(required=False, allow_null=True)
    orderId = serializers.IntegerField(required=False, allow_null=True)
    customerId = serializers.IntegerField(required=False, allow_null=True)
    refundAmount = serializers.FloatField(required=False, allow_null=True)
    status = serializers.CharField(required=False, allow_blank=True, allow_null=True)
    refundDate = serializers.DateTimeField(required=False, allow_null=True, format='%Y-%m-%d %H:%M:%S')

    def create(self, validated_data):
        return RefundedPaymentType(**validated_data)
