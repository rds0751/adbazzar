# -*- coding: utf-8 -*-
# Generated by Django 1.10.8 on 2019-02-24 09:14
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('questionpaper', '0006_auto_20190223_1757'),
    ]

    operations = [
        migrations.CreateModel(
            name='ReadingAnswer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ans', models.CharField(max_length=1000, null=True)),
            ],
        ),
    ]
