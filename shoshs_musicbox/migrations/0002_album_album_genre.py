# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shoshs_musicbox', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='album',
            name='album_genre',
            field=models.CharField(default='', max_length=25),
            preserve_default=False,
        ),
    ]
