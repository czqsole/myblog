# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-01-07 14:13
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pub_time', models.DateField(verbose_name='date published')),
                ('title', models.CharField(max_length=100)),
                ('summary', models.TextField()),
                ('article', models.TextField()),
            ],
        ),
    ]
