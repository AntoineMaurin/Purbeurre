from django.test import TestCase, RequestFactory, Client
from django.contrib.auth.models import User
from favourites.views import *
from django.urls import reverse
from django.contrib import auth
from purbeurre.models import Product
from favourites.models import Favourite


class FavouritesViewsTest(TestCase):

    def setUp(self):
        self.client = Client()
        self.client.post('/accounts/register', {
            'email': 'test@test.com',
            'pw1': 'testtest',
            'pw2': 'testtest'
        })
        self.assertEquals(User.objects.count(), 1)

        response = self.client.post('/accounts/login', {
            'username': 'test@test.com',
            'password': 'testtest'
        })
        self.user = User.objects.get(username='test@test.com')

        self.product = self.create_product()

    def create_product(self):
        category = Category.objects.create(name='pates a tartiner aux noisettes '
                                     'et au cacao')

        Product.objects.create(name='Pâte à tartiner - Gerblé - 220g',
                               nutriscore='a',
                               url='https://fr.openfoodfacts.org/produit/31756'
                                   '81105393/pate-a-tartiner-gerble',
                               image_url='https://static.openfoodfacts.org/im'
                                         'ages/products/317/568/110/5393/front'
                                         '_fr.18.400.jpg',
                               fat_100g=6.6,
                               saturated_fat_100g=0.68,
                               sugars_100g=6.1,
                               salt_100g=0.13,
                               category=category
                               )

        return Product.objects.get(name='Pâte à tartiner - Gerblé - 220g')


    def test_myfood_page_if_auth(self):

        response = self.client.get('/myfood')
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'my_food.html')

    def test_myfood_page_if_not_auth(self):

        self.client.get('/accounts/logout')

        response = self.client.get('/myfood')
        self.assertEquals(response.status_code, 302)
        self.assertRedirects(response, '/accounts/login?next=/myfood')


    def test_save_if_auth(self):

        response = self.client.get('/save/{}'.format(self.product.id),
                                   HTTP_REFERER='/results?user_search=nutella')
        self.assertEquals(response.status_code, 302)
        self.assertRedirects(response, '/results?user_search=nutella')

        f = Favourite.objects.filter(user=self.user, product=self.product)
        self.assertEquals(f.count(), 1)

    def test_save_if_not_auth(self):

        self.client.get('/accounts/logout')

        response = self.client.get('/save/1')
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, '/accounts/login?next=/save/1')

    def test_remove(self):
        """This test creates a product and its category, adds them in test
        database, then adds it to our user's favourites, asserts that he now
        has this one product in favourites, then removes it and asserts that
        the user has no longer this product in his favourites. """

        Favourite.objects.create(user=self.user, product=self.product)

        f = Favourite.objects.filter(user=self.user, product=self.product)

        self.assertEquals(f.count(), 1)

        response = self.client.get('/remove/{}'.format(self.product.id),
                                   HTTP_REFERER='/myfood')

        f = Favourite.objects.filter(user=self.user, product=self.product)

        self.assertEquals(f.count(), 0)

        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, '/myfood')

    def test_remove_if_not_auth(self):

        self.client.get('/accounts/logout')

        response = self.client.get('/remove/{}'.format(self.product.id),
                                   HTTP_REFERER='/accounts/login')

        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, '/accounts/login'
                                       '?next=/remove/{}'.format(self.product.id))

    def test_my_food_page(self):

        response = self.client.get('/myfood')

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'my_food.html')

    def test_my_food_page_if_not_auth(self):

        self.client.get('/accounts/logout')

        response = self.client.get('/myfood')

        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, '/accounts/login?next=/myfood')
