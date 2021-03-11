from decimal import Decimal

import catalogs_pb2
import catalogs_pb2_grpc
import grpc
from django.db import models
from django.utils import timezone


class Order(models.Model):
    user_id = models.PositiveIntegerField()
    created = models.DateTimeField(auto_now=timezone.now)

    @property
    def total(self):
        return sum([item.value for item in self.items.all()])

    def __str__(self):
        return f'{self.id}'


class Item(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='items')
    quantity = models.PositiveIntegerField()
    product_id = models.PositiveIntegerField()

    @property
    def value(self):
        with grpc.insecure_channel('catalogs_web:50051') as channel:
            stub = catalogs_pb2_grpc.ProductControllerStub(channel)
            product = stub.Retrieve(catalogs_pb2.ProductRetrieveRequest(id=self.product_id))
        return self.quantity * Decimal(product.value)

    def __str__(self):
        return f'{self.id}'
