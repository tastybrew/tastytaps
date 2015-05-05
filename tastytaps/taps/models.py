from django.contrib.auth.models import User
from django.db import models


class Beer(models.Model):
    name = models.CharField(max_length=200)
    summary = models.TextField()
    description = models.TextField(blank=True)
    style = models.CharField(max_length=100)
    abv = models.DecimalField(max_digits=4, decimal_places=2, blank=True,
                              null=True)
    ibu = models.PositiveSmallIntegerField(blank=True, null=True)
    srm = models.PositiveSmallIntegerField(blank=True, null=True)
    # TODO: image - for pictures or bottle labels (icon, larger image)
    # Brewery info
    brewery_name = models.CharField(max_length=100)
    brewery_city = models.CharField(max_length=100, blank=True)
    brewery_state = models.CharField(max_length=50, blank=True)
    brewery_country = models.CharField(max_length=100, blank=True)
    # TODO: Image for logo?

    def __unicode__(self):
        return self.name


class Price(models.Model):
    beer = models.ForeignKey(Beer, related_name='prices')
    size = models.CharField(max_length=25)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    # TODO: Add image for glassware for display.

    def __unicode__(self):
        return self.size


class Taproom(models.Model):
    name = models.CharField(max_length=200)
    num_taps = models.PositiveSmallIntegerField()
    address = models.TextField(blank=True)
    users = models.ManyToManyField(User, related_name='taprooms')

    def __unicode__(self):
        return self.name


class Taps(models.Model):
    beer = models.ForeignKey(Beer)
    taproom = models.ForeignKey(Taproom, related_name='taps')
    tap_number = models.PositiveSmallIntegerField()
