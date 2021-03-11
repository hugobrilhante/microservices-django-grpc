from rest_framework import serializers


class ProductSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    name = serializers.CharField()
    value = serializers.DecimalField(max_digits=10, decimal_places=2)


class ItemSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    quantity = serializers.IntegerField()
    product_id = serializers.IntegerField()
    order = serializers.IntegerField()
    value = serializers.DecimalField(max_digits=10, decimal_places=2)


class OrderSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    user_id = serializers.IntegerField()
    items = ItemSerializer(many=True)
