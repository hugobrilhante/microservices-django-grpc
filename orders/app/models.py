from collections import namedtuple

from django.db import models
from django.utils import timezone

Product = namedtuple('Product', ["name", "value"])


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
        # TODO: get product of catalog
        product = Product('Product', 1)
        return self.quantity * product.value

    def __str__(self):
        return f'{self.id}'
