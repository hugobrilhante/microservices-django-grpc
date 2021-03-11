import catalogs_pb2
from django_grpc_framework import proto_serializers

from .models import Product


class ProductProtoSerializer(proto_serializers.ModelProtoSerializer):
    class Meta:
        model = Product
        proto_class = catalogs_pb2.Product
        fields = ['id', 'name', 'value']
