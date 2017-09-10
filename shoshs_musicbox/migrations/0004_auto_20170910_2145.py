# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shoshs_musicbox', '0003_track_youtube_link'),
    ]

    operations = [
        migrations.AlterField(
            model_name='track',
            name='youtube_link',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
