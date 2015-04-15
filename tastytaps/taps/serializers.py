from rest_framework import serializers

from .models import Price, Taps


class PriceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Price
        fields = ('size', 'price')


class TapsSerializer(serializers.ModelSerializer):
    prices = PriceSerializer(many=True)

    class Meta:
        model = Taps

    def create(self, data):
        prices = data.pop('prices')
        tap = Taps.objects.create(**data)
        for price in prices:
            Price.objects.create(tap=tap, **price)
        return tap

    def update(self, tap, data):
        prices = data.pop('prices')
        for k, v in data.items():
            setattr(tap, k, v)
        tap.prices.all().delete()
        for price in prices:
            Price.objects.create(tap=tap, **price)
        tap.save()
        return tap
