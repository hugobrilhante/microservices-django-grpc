import grpc
import catalogs_pb2
import catalogs_pb2_grpc
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import ProductSerializer


class ProductAPIView(APIView):

    def get(self, request, *args, **kwargs):
        with grpc.insecure_channel('catalogs_web:50051') as channel:
            stub = catalogs_pb2_grpc.ProductControllerStub(channel)
            products = stub.List(catalogs_pb2.ProductListRequest())
            serializer = ProductSerializer(instance=products, many=True)
            return Response(serializer.data)
