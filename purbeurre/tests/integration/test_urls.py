from django.urls import reverse, resolve
from django.test import TestCase
from purbeurre.views import *


class ProductsTest(TestCase):

    def test_home_url_is_resolved(self):
        url = reverse(homepage)
        self.assertEqual(resolve(url).func, homepage)

    def test_results_url_is_resolved(self):
        url = reverse(search)
        self.assertEqual(resolve(url).func, search)

    def test_account_url_is_resolved(self):
        url = reverse(accountpage)
        self.assertEqual(resolve(url).func, accountpage)

    def test_product_url_is_resolved(self):
        url = reverse(productpage, args=[35067])
        self.assertEqual(resolve(url).func, productpage)
