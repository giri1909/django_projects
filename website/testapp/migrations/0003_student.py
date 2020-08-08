# -*- coding: utf-8 -*-
# Generated by Django 1.11.17 on 2020-06-03 05:13
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testapp', '0002_auto_20200603_1040'),
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sname', models.CharField(max_length=30)),
                ('course', models.CharField(max_length=30)),
                ('phno', models.IntegerField()),
                ('email', models.EmailField(max_length=80)),
            ],
        ),
    ]