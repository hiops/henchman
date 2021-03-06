# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-11-08 14:56
from __future__ import unicode_literals

import os

from django.db import migrations
from django.core import management
from django.core.management.commands import loaddata


def load_data(*args):
    management.call_command(loaddata.Command(), os.path.join('authentication', 'fixtures', 'user.json'))


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(load_data),
    ]
