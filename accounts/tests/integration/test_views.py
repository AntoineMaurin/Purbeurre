from django.test import TestCase, RequestFactory, Client
from django.contrib.auth.models import User
from accounts.forms import UserRegisterForm, UserLoginForm
from accounts.views import *
from django.urls import reverse
from django.contrib import auth


class AccountsViewsTest(TestCase):

    def setUp(self):
        self.client = Client()

    def test_login_get(self):
        response = self.client.get('/accounts/login')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'login.html')
        self.failUnless(isinstance(response.context['form'], UserLoginForm))

    def test_register_get(self):
        response = self.client.get('/accounts/register')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'registration.html')
        self.failUnless(isinstance(response.context['form'], UserRegisterForm))

    def test_logout_get(self):
        response = self.client.get('/accounts/logout')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'login.html')

    def test_register_success_post(self):
        response = self.client.post('/accounts/register', {
            'email': 'thetest@test.com',
            'pw1': 'testtest',
            'pw2': 'testtest'
        })

        self.assertEqual(response.status_code, 200)
        self.assertEqual(User.objects.count(), 1)
        self.assertTemplateUsed(response, 'login.html')

    def test_register_fails_post(self):
        response = self.client.post('/accounts/register', {
            'email': 'anothertest@test.com',
            'pw1': 'testtest',
            'pw2': 'wrongconfirm'
        })

        self.assertEqual(response.status_code, 200)
        self.assertEquals(User.objects.count(), 0)
        self.assertTemplateUsed(response, 'registration.html')
        self.failUnless(isinstance(response.context['form'], UserRegisterForm))

    def test_login_success_post(self):

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

        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, '/')

        user = auth.get_user(self.client)
        self.assertEquals(user.is_authenticated, True)

    def test_login_fails_post(self):

        self.client.post('/accounts/register', {
            'email': 'test@test.com',
            'pw1': 'testtest',
            'pw2': 'testtest'
        })
        self.assertEquals(User.objects.count(), 1)

        response = self.client.post('/accounts/login', {
            'username': 'test@test.com',
            'password': 'wrongpassword'
        })

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'login.html')

        user = auth.get_user(self.client)
        self.assertEquals(user.is_authenticated, False)

    def test_logout_post(self):
        """Creates account, connect, and disconnect to check the efficiency of
        the logout view"""
        
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

        user = auth.get_user(self.client)
        self.assertEquals(user.is_authenticated, True)

        response = self.client.get('/accounts/logout')
        disconnected_user = auth.get_user(self.client)
        self.assertEquals(disconnected_user.is_authenticated, False)
