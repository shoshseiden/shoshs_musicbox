# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shoshs_musicbox', '0005_auto_20170910_2154'),
    ]

    operations = [
        migrations.AlterField(
            model_name='track',
            name='youtube_link',
            field=models.CharField(max_length=100, blank=True),
        ),
    ]
