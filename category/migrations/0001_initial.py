# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('title', models.CharField(max_length=120, null=True)),
                ('slug', models.CharField(max_length=120, null=True)),
                ('description', models.TextField()),
                ('tags', models.TextField()),
            ],
            options={
                'db_table': 'category',
            },
        ),
    ]
