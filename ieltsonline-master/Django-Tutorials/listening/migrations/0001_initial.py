# -*- coding: utf-8 -*-
# Generated by Django 1.10.8 on 2019-02-18 16:03
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AudioMain',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Question_Name', models.CharField(default='Listening Part', max_length=50)),
                ('Instruction', models.TextField(default='instructions', max_length=2000)),
                ('audio_file', models.FileField(help_text='Allowed type - .mp3, .wav, .ogg', null=True, upload_to='audiofolder/')),
            ],
        ),
        migrations.CreateModel(
            name='Fillup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Question_Name', models.CharField(default='Fillup Question', max_length=50)),
                ('Instruction', models.TextField(default='your instructions', max_length=2000)),
                ('Question', models.TextField(default='Your questions', max_length=100)),
                ('audio', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='audioFill', to='listening.AudioMain')),
            ],
        ),
        migrations.CreateModel(
            name='FillupQue',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('part1', models.CharField(max_length=100, null=True)),
                ('part2', models.CharField(max_length=100, null=True)),
                ('linked', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='linkedfillup', to='listening.Fillup')),
            ],
        ),
        migrations.CreateModel(
            name='MapMatch',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('map', models.ImageField(null=True, upload_to='audiomap/')),
                ('Question_Name', models.CharField(default='Map Question', max_length=50)),
                ('Instruction', models.TextField(default='your instructions', max_length=2000)),
                ('Question', models.TextField(default='Your questions', max_length=100)),
                ('audio', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='audioMap', to='listening.AudioMain')),
            ],
        ),
        migrations.CreateModel(
            name='MapMatchQues',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('part', models.CharField(max_length=100, null=True)),
                ('linked', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='linkedmap', to='listening.MapMatch')),
            ],
        ),
        migrations.CreateModel(
            name='Matching',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Question_Name', models.CharField(default='Matching Question', max_length=50)),
                ('Instruction', models.TextField(default='your instructions', max_length=2000)),
                ('l1', models.CharField(max_length=100, null=True)),
                ('l2', models.CharField(max_length=100, null=True)),
                ('l3', models.CharField(blank=True, max_length=100, null=True)),
                ('l4', models.CharField(blank=True, max_length=100, null=True)),
                ('l5', models.CharField(blank=True, max_length=100, null=True)),
                ('l6', models.CharField(blank=True, max_length=100, null=True)),
                ('l7', models.CharField(blank=True, max_length=100, null=True)),
                ('l8', models.CharField(blank=True, max_length=100, null=True)),
                ('l9', models.CharField(blank=True, max_length=100, null=True)),
                ('l10', models.CharField(blank=True, max_length=100, null=True)),
                ('r1', models.CharField(max_length=100, null=True)),
                ('r2', models.CharField(max_length=100, null=True)),
                ('r3', models.CharField(blank=True, max_length=100, null=True)),
                ('r4', models.CharField(blank=True, max_length=100, null=True)),
                ('r5', models.CharField(blank=True, max_length=100, null=True)),
                ('r6', models.CharField(blank=True, max_length=100, null=True)),
                ('r7', models.CharField(blank=True, max_length=100, null=True)),
                ('r8', models.CharField(blank=True, max_length=100, null=True)),
                ('r9', models.CharField(blank=True, max_length=100, null=True)),
                ('r10', models.CharField(blank=True, max_length=100, null=True)),
                ('audio', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='audioMatch', to='listening.AudioMain')),
            ],
        ),
        migrations.CreateModel(
            name='MCQ',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Question_Name', models.CharField(default='MCQ Question', max_length=50)),
                ('Instruction', models.TextField(default='your instructions', max_length=2000)),
                ('passage', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='audiomcq', to='listening.AudioMain')),
            ],
        ),
        migrations.CreateModel(
            name='MCQQues',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Question', models.TextField(default='Your questions', max_length=100)),
                ('option1', models.CharField(max_length=100, null=True)),
                ('option2', models.CharField(max_length=100, null=True)),
                ('option3', models.CharField(blank=True, max_length=100, null=True)),
                ('option4', models.CharField(blank=True, max_length=100, null=True)),
                ('option5', models.CharField(blank=True, max_length=100, null=True)),
                ('option6', models.CharField(blank=True, max_length=100, null=True)),
                ('linked', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='linkedmcq', to='listening.MCQ')),
            ],
        ),
        migrations.CreateModel(
            name='Summary',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Question_Name', models.CharField(default='audio Question', max_length=50)),
                ('Instruction', models.TextField(default='your instructions', max_length=2000)),
                ('part1', models.CharField(max_length=100, null=True)),
                ('part2', models.CharField(max_length=100, null=True)),
                ('part3', models.CharField(blank=True, max_length=100, null=True)),
                ('part4', models.CharField(blank=True, max_length=100, null=True)),
                ('part5', models.CharField(blank=True, max_length=100, null=True)),
                ('part6', models.CharField(blank=True, max_length=100, null=True)),
                ('part7', models.CharField(blank=True, max_length=100, null=True)),
                ('audio', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='audiosumm', to='listening.AudioMain')),
            ],
        ),
    ]