from django.conf.urls import url, include
from django.contrib import admin


from . import views

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', views.index, name='home'),
    url(r'^artistlibrary/$', views.ArtistLibraryView.as_view(), name='artist_library'),
    url(r'^artistlibrary/artist/(?P<artist_id>[0-9]+)/$', views.artist, name='artist'),
    url(r'^artist/(?P<artist_id>[0-9]+)/album/(?P<album_id>[0-9]+)/$', views.album, name='album'),
    url(r'^bloglist/$', views.BlogListView.as_view(), name='blog_list'),
    url(r'^bloglist/blog/(?P<blog_id>[0-9]+)/$', views.blog, name='blog'),
]
