# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Price',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('size', models.CharField(max_length=25)),
                ('price', models.DecimalField(max_digits=5, decimal_places=2)),
            ],
        ),
        migrations.CreateModel(
            name='Taps',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200)),
                ('summary', models.TextField()),
                ('description', models.TextField(blank=True)),
                ('style', models.CharField(max_length=100)),
                ('abv', models.DecimalField(null=True, max_digits=4, decimal_places=2, blank=True)),
                ('ibu', models.PositiveSmallIntegerField(null=True, blank=True)),
                ('srm', models.PositiveSmallIntegerField(null=True, blank=True)),
                ('brewery_name', models.CharField(max_length=100)),
                ('brewery_city', models.CharField(max_length=100, blank=True)),
                ('brewery_state', models.CharField(max_length=50, blank=True)),
                ('brewery_country', models.CharField(max_length=100, blank=True)),
            ],
        ),
        migrations.AddField(
            model_name='price',
            name='tap',
            field=models.ForeignKey(related_name='prices', to='taps.Taps'),
        ),
    ]
