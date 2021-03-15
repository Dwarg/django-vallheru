# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-02-16 20:55
from __future__ import unicode_literals

from decimal import Decimal
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('players', '0006_auto_20160215_2318'),
    ]

    operations = [
        migrations.AddField(
            model_name='playerskills',
            name='carpentry',
            field=models.DecimalField(decimal_places=2, default=Decimal('0.01000000000000000020816681711721685132943093776702880859375'), max_digits=6),
        ),
    ]