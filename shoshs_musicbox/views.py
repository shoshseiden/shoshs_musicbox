from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, Http404
from django import template
from django.template.loader import get_template
from django.template import RequestContext, loader
from django.views import generic

from .models import Artist, Album, Track, Blog


def index(request):
    template_name = 'shoshs_musicbox/index.html'
    return render(request, template_name)


class ArtistLibraryView(generic.ListView):
    template_name = 'shoshs_musicbox/artistlibrary.html'
    context_object_name = 'artist_list'

    def get_queryset(self):
        return Artist.objects.order_by('artist_name')


def artist(request, artist_id):
    selected_artist = get_object_or_404(Artist, pk=artist_id)
    return render(request, 'shoshs_musicbox/artist.html', {'artist': selected_artist})


def album(request, artist_id, album_id):
    p = get_object_or_404(Artist, pk=artist_id)
    try:
        selected_album = p.album_set.get(pk=album_id)
    except Album.DoesNotExist:
        raise Http404("Album does not exist")
    else:
        return render(request, "shoshs_musicbox/album.html", {'album': selected_album})


class BlogListView(generic.ListView):
    template_name = 'shoshs_musicbox/bloglist.html'
    context_object_name = 'blog_list'

    def get_queryset(self):
        return Blog.objects.order_by('blog_date')


def blog(request, blog_id):
    selected_blog = get_object_or_404(Blog, pk=blog_id)
    return render(request, 'shoshs_musicbox/blog.html', {'blog': selected_blog})
