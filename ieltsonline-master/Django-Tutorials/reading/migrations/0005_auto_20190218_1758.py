# -*- coding: utf-8 -*-
# Generated by Django 1.10.8 on 2019-02-18 12:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reading', '0004_auto_20190218_1753'),
    ]

    operations = [
        migrations.AlterField(
            model_name='passagemain',
            name='Instruction',
            field=models.TextField(default='instructions', max_length=2000),
        ),
        migrations.AlterField(
            model_name='yesnonotgiven',
            name='Instruction',
            field=models.TextField(default='your instructions', max_length=2000),
        ),
    ]
