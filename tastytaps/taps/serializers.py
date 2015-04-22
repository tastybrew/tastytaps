from rest_framework import serializers

from .models import Beer, Price


class PriceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Price
        fields = ('size', 'price')


class BeerSerializer(serializers.ModelSerializer):
    prices = PriceSerializer(many=True)

    class Meta:
        model = Beer

    def create(self, data):
        prices = data.pop('prices')
        beer = Beer.objects.create(**data)
        for price in prices:
            Price.objects.create(beer=beer, **price)
        return beer

    def update(self, beer, data):
        prices = data.pop('prices')
        for k, v in data.items():
            setattr(beer, k, v)
        beer.prices.all().delete()
        for price in prices:
            Price.objects.create(beer=beer, **price)
        beer.save()
        return beer
