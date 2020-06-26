from django.test import TestCase, Client
from django.contrib.auth.models import User
from purbeurre.models import Product, Category


class PurbeurreViewsTest(TestCase):

    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username='test@test.com',
                                             email='test@test.com',
                                             password='testtest')

        self.client.post('/accounts/login', {
            'username': 'test@test.com',
            'password': 'testtest'
        })

        self.product = self.create_product()

    def create_product(self):
        category = Category.objects.create(name='pates a tartiner aux '
                                                'noisettes et au cacao')

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

    def test_product_page(self):

        response = self.client.get('/product/{}'.format(self.product.id))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'product_page.html')

    def test_home_page(self):

        response = self.client.get('')

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'home.html')

    def test_account_page(self):

        response = self.client.get('/account')

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'my_account.html')

    def test_account_page_if_not_auth(self):

        self.client.get('/accounts/logout')

        response = self.client.get('/account')

        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, '/accounts/login?next=/account')

    def test_search(self):

        response = self.client.get('/results?user_search=nutella')

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'results.html')

    def test_legaldisclaimerpage(self):

        response = self.client.get('/legal')

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'legal_disclaimer.html')
