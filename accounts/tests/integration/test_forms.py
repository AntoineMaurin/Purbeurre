from accounts.forms import UserRegisterForm, UserLoginForm
from django.test import TestCase, Client


class AccountsFormsTest(TestCase):

    def setUp(self):
        self.client = Client()

    def test_register_valid_data(self):
        form = UserRegisterForm(data={
            'email': 'thetest@test.com',
            'pw1': 'testtest',
            'pw2': 'testtest'
        })

        self.assertTrue(form.is_valid())

    def test_register_no_data(self):
        form = UserRegisterForm(data={})

        self.assertFalse(form.is_valid())

    def test_login_valid_data(self):
        self.client.post('/accounts/register', {
            'email': 'thetest@test.com',
            'pw1': 'testtest',
            'pw2': 'testtest'
        })

        form = UserLoginForm(data={
            'username': 'thetest@test.com',
            'password': 'testtest',
        })

        self.assertTrue(form.is_valid())

    def test_login_no_data(self):
        form = UserLoginForm(data={})

        self.assertFalse(form.is_valid())
