# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('taps', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Taps',
            new_name='Beer',
        ),
        migrations.RenameField(
            model_name='price',
            old_name='tap',
            new_name='beer',
        ),
    ]
