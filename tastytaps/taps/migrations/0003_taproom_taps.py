# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('taps', '0002_rename_taps_to_beer'),
    ]

    operations = [
        migrations.CreateModel(
            name='Taproom',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200)),
                ('num_taps', models.PositiveSmallIntegerField()),
                ('address', models.TextField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Taps',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('tap_number', models.PositiveSmallIntegerField()),
                ('beer', models.ForeignKey(to='taps.Beer')),
                ('taproom', models.ForeignKey(related_name='taps', to='taps.Taproom')),
            ],
        ),
    ]
