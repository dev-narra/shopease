from rest_framework import serializers

from dsu.dsu_gen.openapi.decorator.deserialize import deserialize
from dsu.dsu_gen.openapi.utils.type_file_utils import get_type_object
from dsu.dsu_gen.openapi.utils.type_file_utils import get_type_list_object
from dsu.dsu_gen.openapi.fields.collection_format_field import CollectionFormatField


class BasicProductType(object):
    def __init__(self, description, name, stock_quantity, exp_date, mfg_date, price, category=None,  **kwargs):
        self.description = description
        self.name = name
        self.stock_quantity = stock_quantity
        self.exp_date = exp_date
        self.mfg_date = mfg_date
        self.price = price
        self.category = category

    def __str__(self):
        from dsu.dsu_gen.openapi.utils.get_unicode_str import get_unicode_str
        return get_unicode_str(self).encode('utf-8')

    def __getitem__(self, item):
        return getattr(self, item)


class BasicProductSerializer(serializers.Serializer):
    name = serializers.CharField()
    description = serializers.CharField()
    price = serializers.FloatField()
    mfg_date = serializers.CharField()
    exp_date = serializers.CharField()
    category = serializers.CharField(required=False, allow_blank=True, allow_null=True)
    stock_quantity = serializers.FloatField()

    def create(self, validated_data):
        return BasicProductType(**validated_data)
