# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-08-18 16:49
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('enterprises', '0002_enterprise_name'),
    ]

    operations = [
        migrations.RenameField(
            model_name='enterprise',
            old_name='name',
            new_name='enterprise_name',
        ),
    ]
