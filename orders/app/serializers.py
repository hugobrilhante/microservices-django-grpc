import items_pb2
import orders_pb2
from django_grpc_framework import proto_serializers

from .models import Item, Order


class ItemProtoSerializer(proto_serializers.ModelProtoSerializer):
    class Meta:
        model = Item
        proto_class = items_pb2.Item
        fields = ['id', 'quantity', 'product_id', 'order', 'value']


class OrderProtoSerializer(proto_serializers.ModelProtoSerializer):
    items = ItemProtoSerializer(required=False, many=True)

    class Meta:
        model = Order
        proto_class = orders_pb2.Order
        fields = ['id', 'user_id', 'items']

    def to_internal_value(self, data):
        items = data.pop('items')
        ret = super().to_internal_value(data)
        ret['items'] = items
        return ret

    def create(self, validated_data):
        items = validated_data.pop('items')
        order = super().create(validated_data)
        for item in items:
            item.update(order=order.id)
        item_serializer = ItemProtoSerializer(data=items, many=True)
        item_serializer.is_valid()
        item_serializer.save()
        return order
