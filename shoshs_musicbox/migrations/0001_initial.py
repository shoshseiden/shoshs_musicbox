# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Album',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('album_name', models.CharField(max_length=50)),
                ('album_year', models.IntegerField(null=True)),
                ('album_review', models.TextField(null=True)),
                ('album_cover', models.ImageField(upload_to=b'album_covers')),
            ],
        ),
        migrations.CreateModel(
            name='Artist',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('artist_name', models.CharField(max_length=50)),
                ('artist_picture', models.ImageField(upload_to=b'artist_pictures')),
            ],
        ),
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('blog_date', models.DateTimeField(verbose_name=b'date posted')),
                ('blog_title', models.CharField(max_length=100)),
                ('blog_post', models.TextField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Track',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('track_title', models.CharField(max_length=100)),
                ('track_number', models.IntegerField(null=True)),
                ('album', models.ForeignKey(to='shoshs_musicbox.Album')),
            ],
        ),
        migrations.AddField(
            model_name='album',
            name='artist',
            field=models.ForeignKey(to='shoshs_musicbox.Artist'),
        ),
    ]
