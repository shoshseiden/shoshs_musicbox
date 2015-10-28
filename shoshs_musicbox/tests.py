import unittest
from django.core.urlresolvers import reverse
from django.test import TestCase, Client
from .models import Artist, Album, Track, Blog
from django.core.files import File


class ViewsTest(TestCase):
    def setUp(self):
        self.client = Client()

    def test_artist_library(self):
        Artist.objects.create(artist_name="Test Artist")
        url = reverse('musicbox:artistLibrary')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_blog_list(self):
        Blog.objects.create(blog_title="Blog Test", blog_date="2015-10-28 13:40", blog_post="Blah")
        url = reverse('musicbox:blogList')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
