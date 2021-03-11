from rest_framework import serializers


class ProductSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    name = serializers.CharField()
    value = serializers.DecimalField(max_digits=10, decimal_places=2)