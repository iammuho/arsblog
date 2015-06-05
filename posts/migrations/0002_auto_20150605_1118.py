# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='posts',
            name='publish_date',
            field=models.DateTimeField(default=datetime.datetime(2015, 6, 5, 11, 18, 26, 269946, tzinfo=utc), auto_now_add=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='posts',
            name='update_date',
            field=models.DateTimeField(default=datetime.datetime(2015, 6, 5, 11, 18, 32, 398137, tzinfo=utc), auto_now=True),
            preserve_default=False,
        ),
    ]
