from django_grpc_framework import generics

from .models import Product
from .serializers import ProductProtoSerializer


class ProductService(generics.ModelService):
    """
    gRPC service that allows users to be retrieved or updated.
    """
    queryset = Product.objects.all().order_by('id')
    serializer_class = ProductProtoSerializer
