from django.db import models


class Taps(models.Model):
    name = models.CharField(max_length=200)
    summary = models.TextField()
    description = models.TextField(blank=True)
    brewery = models.ForeignKey('Brewery', related_name='brewery')
    style = models.CharField(max_length=100)
    abv = models.DecimalField(max_digits=4, decimal_places=2, blank=True,
                              null=True)
    ibu = models.PositiveSmallIntegerField(blank=True, null=True)
    srm = models.PositiveSmallIntegerField(blank=True, null=True)
    price = models.ForeignKey('Price', related_name='prices')
    # TODO: image - for pictures or bottle labels (icon, larger image)


class Brewery(models.Model):
    name = models.CharField(max_length=100)
    city = models.CharField(max_length=100, blank=True)
    state = models.CharField(max_length=50, blank=True)
    country = models.CharField(max_length=100, blank=True)
    # TODO: Image for logo?


class Price(models.Model):
    size = models.CharField(max_length=25)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    # TODO: Add image for glassware for display.
