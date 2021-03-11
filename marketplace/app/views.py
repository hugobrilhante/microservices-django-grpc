import catalogs_pb2
import catalogs_pb2_grpc
import grpc
import orders_pb2
import orders_pb2_grpc
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import ProductSerializer, OrderSerializer


class ProductAPIView(APIView):

    def get(self, request, *args, **kwargs):
        with grpc.insecure_channel('catalogs_web:50051') as channel:
            stub = catalogs_pb2_grpc.ProductControllerStub(channel)
            products = stub.List(catalogs_pb2.ProductListRequest())
            serializer = ProductSerializer(instance=products, many=True)
            return Response(serializer.data)


class OrderAPIView(APIView):

    def get(self, request, *args, **kwargs):
        with grpc.insecure_channel('orders_web:50051') as channel:
            stub = orders_pb2_grpc.OrderControllerStub(channel)
            orders = stub.List(orders_pb2.OrderListRequest())
            serializer = OrderSerializer(orders, many=True)
            return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        with grpc.insecure_channel('orders_web:50051') as channel:
            stub = orders_pb2_grpc.OrderControllerStub(channel)
            order = stub.Create(orders_pb2.Order(**request.data))
            serializer = OrderSerializer(order)
            return Response(serializer.data)
