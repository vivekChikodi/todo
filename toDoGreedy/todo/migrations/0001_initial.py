# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-03-19 06:14
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='addBookmark',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bookmark_tag', models.CharField(max_length=200)),
                ('bookmark_name', models.CharField(max_length=200)),
                ('bookmark_desc', models.CharField(max_length=500)),
            ],
        ),
    ]