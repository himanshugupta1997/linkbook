# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-06-14 11:42
from __future__ import unicode_literals

from django.db import migrations
import jsonfield.fields


class Migration(migrations.Migration):

    dependencies = [
        ('links', '0006_auto_20170614_0743'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='tags',
            field=jsonfield.fields.JSONField(blank=True, null=True),
        ),
    ]
