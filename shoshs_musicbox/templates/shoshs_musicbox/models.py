from django.db import models


class Artist(models.Model):
    artist_name = models.CharField(max_length=50)
    artist_picture = models.ImageField(upload_to='artist_pictures')

    def __str__(self):
        return self.artist_name


class Album(models.Model):
    artist = models.ForeignKey(Artist)
    album_name = models.CharField(max_length=50)
    album_year = models.IntegerField(null=True)
    album_review = models.TextField(null=True)
    album_cover = models.ImageField(upload_to='album_covers')

    def __str__(self):
        return self.album_name


class Track(models.Model):
    album = models.ForeignKey(Album)
    track_title = models.CharField(max_length=100)
    track_number = models.IntegerField(null=True)

    def __str__(self):
        return self.track_title


class Blog(models.Model):
    blog_date = models.DateTimeField('date posted')
    blog_title = models.CharField(max_length=100)
    blog_post = models.TextField(null=True)

    def __str__(self):
        return self.blog_title
