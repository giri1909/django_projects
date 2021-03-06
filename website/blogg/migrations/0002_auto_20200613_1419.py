# -*- coding: utf-8 -*-
# Generated by Django 1.11.17 on 2020-06-13 08:49
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blogg', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='EnqDB',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('mail', models.CharField(max_length=30)),
                ('mno', models.IntegerField()),
                ('message', models.CharField(max_length=60)),
            ],
        ),
        migrations.AlterField(
            model_name='post',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 6, 13, 8, 49, 36, 253935, tzinfo=utc)),
        ),
    ]
