# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shoshs_musicbox', '0002_album_album_genre'),
    ]

    operations = [
        migrations.AddField(
            model_name='track',
            name='youtube_link',
            field=models.CharField(default=' ', max_length=100),
            preserve_default=False,
        ),
    ]
