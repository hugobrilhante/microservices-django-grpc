from django_grpc_framework import generics

from .models import Item, Order
from .serializers import ItemProtoSerializer, OrderProtoSerializer


class ItemService(generics.ModelService):
    queryset = Item.objects.all().order_by('id')
    serializer_class = ItemProtoSerializer


class OrderService(generics.ModelService):
    queryset = Order.objects.all().order_by('id')
    serializer_class = OrderProtoSerializer
