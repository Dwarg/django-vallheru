# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-02-15 23:09
from __future__ import unicode_literals

from decimal import Decimal
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('players', '0004_playerskills'),
    ]

    operations = [
        migrations.AlterField(
            model_name='playerskills',
            name='alchemy',
            field=models.DecimalField(decimal_places=2, default=Decimal('0.01000000000000000020816681711721685132943093776702880859375'), max_digits=6),
        ),
        migrations.AlterField(
            model_name='playerskills',
            name='archery',
            field=models.DecimalField(decimal_places=2, default=Decimal('0.01000000000000000020816681711721685132943093776702880859375'), max_digits=6),
        ),
        migrations.AlterField(
            model_name='playerskills',
            name='blacksmithing',
            field=models.DecimalField(decimal_places=2, default=Decimal('0.01000000000000000020816681711721685132943093776702880859375'), max_digits=6),
        ),
        migrations.AlterField(
            model_name='playerskills',
            name='breeding',
            field=models.DecimalField(decimal_places=2, default=Decimal('0.01000000000000000020816681711721685132943093776702880859375'), max_digits=6),
        ),
        migrations.AlterField(
            model_name='playerskills',
            name='evasion',
            field=models.DecimalField(decimal_places=2, default=Decimal('0.01000000000000000020816681711721685132943093776702880859375'), max_digits=6),
        ),
        migrations.AlterField(
            model_name='playerskills',
            name='herbalism',
            field=models.DecimalField(decimal_places=2, default=Decimal('0.01000000000000000020816681711721685132943093776702880859375'), max_digits=6),
        ),
        migrations.AlterField(
            model_name='playerskills',
            name='jewellery',
            field=models.DecimalField(decimal_places=2, default=Decimal('0.01000000000000000020816681711721685132943093776702880859375'), max_digits=6),
        ),
        migrations.AlterField(
            model_name='playerskills',
            name='leadership',
            field=models.DecimalField(decimal_places=2, default=Decimal('0.01000000000000000020816681711721685132943093776702880859375'), max_digits=6),
        ),
        migrations.AlterField(
            model_name='playerskills',
            name='melee',
            field=models.DecimalField(decimal_places=2, default=Decimal('0.01000000000000000020816681711721685132943093776702880859375'), max_digits=6),
        ),
        migrations.AlterField(
            model_name='playerskills',
            name='metallurgy',
            field=models.DecimalField(decimal_places=2, default=Decimal('0.01000000000000000020816681711721685132943093776702880859375'), max_digits=6),
        ),
        migrations.AlterField(
            model_name='playerskills',
            name='mining',
            field=models.DecimalField(decimal_places=2, default=Decimal('0.01000000000000000020816681711721685132943093776702880859375'), max_digits=6),
        ),
        migrations.AlterField(
            model_name='playerskills',
            name='perceptivity',
            field=models.DecimalField(decimal_places=2, default=Decimal('0.0200000000000000004163336342344337026588618755340576171875'), max_digits=6),
        ),
        migrations.AlterField(
            model_name='playerskills',
            name='player',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='skills', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='playerskills',
            name='spell_casting',
            field=models.DecimalField(decimal_places=2, default=Decimal('0.01000000000000000020816681711721685132943093776702880859375'), max_digits=6),
        ),
        migrations.AlterField(
            model_name='playerskills',
            name='wood_working',
            field=models.DecimalField(decimal_places=2, default=Decimal('0.01000000000000000020816681711721685132943093776702880859375'), max_digits=6),
        ),
    ]