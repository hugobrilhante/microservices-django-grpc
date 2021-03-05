from django.db import models
from django.utils import timezone


class Payment(models.Model):
    user_id = models.PositiveIntegerField()
    order_id = models.PositiveIntegerField()
    value = models.DecimalField(max_digits=10, decimal_places=2)
    created = models.DateTimeField(auto_now=timezone.now)

    def __str__(self):
        return f'{self.id}'
