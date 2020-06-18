from django.test import TestCase, RequestFactory, Client
from django.contrib.auth.models import User
# from accounts.forms import UserRegisterForm, UserLoginForm
from accounts.views import *


class ProductsTest(TestCase):

    def setUp(self):
        self.request = RequestFactory()
        self.client = Client()
        self.user = User.objects.create_user(username='test_username',
                                             email='test@test.com',
                                             password='testpassword')

    def test_login_get(self):
        response = self.client.get('/accounts/login')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'login.html')

    def test_register_get(self):
        response = self.client.get('/accounts/register')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'registration.html')

    def test_logout_get(self):
        response = self.client.get('/accounts/logout')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'login.html')

    def test_register_adds_user(self):
        response = self.client.post('/accounts/register', {
            'email': 'thetest@test.com',
            'pw1': 'testtest',
            'pw2': 'testtest'
        })
        request = User.objects.get(username='thetest@test.com')
        self.assertEquals(request.username, 'thetest@test.com')
