# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('subscription', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='subscribe',
            name='ip_address',
        ),
        migrations.RemoveField(
            model_name='subscribe',
            name='timestamp',
        ),
        migrations.RemoveField(
            model_name='subscribe',
            name='updated',
        ),
    ]
