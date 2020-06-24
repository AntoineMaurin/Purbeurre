from django.test import TestCase, Client
from django.contrib.auth.models import User
from accounts.forms import UserRegisterForm, UserLoginForm
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

        self.assertEquals(response.status_code, 200)
        self.assertEquals(User.objects.count(), 0)
        self.assertTemplateUsed(response, 'registration.html')
        self.failUnless(isinstance(response.context['form'], UserRegisterForm))

    def test_login_success_post(self):

        User.objects.create_user(username='test@test.com',
                                 email='test@test.com',
                                 password='testtest')

        response = self.client.post('/accounts/login', {
            'username': 'test@test.com',
            'password': 'testtest'
        })

        self.assertEquals(response.status_code, 302)
        self.assertRedirects(response, '/')

        user = auth.get_user(self.client)
        self.assertEquals(user.is_authenticated, True)

    def test_login_fails_post(self):

        User.objects.create_user(username='test@test.com',
                                 email='test@test.com',
                                 password='testtest')

        response = self.client.post('/accounts/login', {
            'username': 'test@test.com',
            'password': 'wrongpassword'
        })

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'login.html')

        user = auth.get_user(self.client)
        self.assertFalse(user.is_authenticated)

    def test_logout(self):
        """Creates account, connect, and disconnect to check the efficiency of
        the logout view"""

        User.objects.create_user(username='test@test.com',
                                 email='test@test.com',
                                 password='testtest')

        self.client.post('/accounts/login', {
            'username': 'test@test.com',
            'password': 'testtest'
        })

        user = auth.get_user(self.client)
        self.assertTrue(user.is_authenticated)

        self.client.get('/accounts/logout')
        disconnected_user = auth.get_user(self.client)
        self.assertFalse(disconnected_user.is_authenticated)
