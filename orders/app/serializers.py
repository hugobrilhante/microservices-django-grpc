import items_pb2
import orders_pb2
from django_grpc_framework import proto_serializers

from .models import Item, Order


class ItemProtoSerializer(proto_serializers.ModelProtoSerializer):
    class Meta:
        model = Item
        proto_class = items_pb2.Item
        fields = ['id', 'quantity', 'product_id', 'order']


class OrderProtoSerializer(proto_serializers.ModelProtoSerializer):
    items = ItemProtoSerializer(many=True)

    class Meta:
        model = Order
        proto_class = orders_pb2.Order
        fields = ['id', 'user_id', 'items']
