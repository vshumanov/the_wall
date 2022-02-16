from rest_framework import serializers


class QuantitySerializer(serializers.Serializer):
    day = serializers.IntegerField()
    ice_amount = serializers.IntegerField()


class CostSerializer(serializers.Serializer):
    day = serializers.IntegerField()
    cost = serializers.IntegerField()
