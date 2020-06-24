from django.urls import reverse, resolve
from django.test import TestCase
from favourites.views import save, remove, myfoodpage


class FavouritesUrlsTest(TestCase):

    def test_save_url_is_resolved(self):
        url = reverse(save, args=[35067])
        self.assertEqual(resolve(url).func, save)

    def test_remove_url_is_resolved(self):
        url = reverse(remove, args=[35067])
        self.assertEqual(resolve(url).func, remove)

    def test_myfood_url_is_resolved(self):
        url = reverse(myfoodpage)
        self.assertEqual(resolve(url).func, myfoodpage)
