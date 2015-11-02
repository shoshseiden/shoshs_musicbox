from django.contrib import admin
from .models import Artist, Album, Track, Blog


class AlbumInline(admin.TabularInline):
    model = Album
    extra = 1


class TrackInline(admin.TabularInline):
    model = Track
    extra = 1


class ArtistAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Images', {'fields': ['artist_picture']}),
        ('Artist Information', {'fields': ['artist_name']}),
    ]
    inlines = [AlbumInline]


class AlbumAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Images', {'fields': ['album_cover']}),
        ('Album Information', {'fields': ['album_name', 'album_genre',
         'album_year', 'album_review']}),
    ]
    inlines = [TrackInline]


class TrackAdmin(admin.ModelAdmin):
    fields = ['track_number', 'track_title']


class BlogAdmin(admin.ModelAdmin):
    fields = ['blog_title', 'blog_date', 'blog_post']

admin.site.register(Artist, ArtistAdmin)
admin.site.register(Album, AlbumAdmin)
admin.site.register(Track, TrackAdmin)
admin.site.register(Blog, BlogAdmin)
