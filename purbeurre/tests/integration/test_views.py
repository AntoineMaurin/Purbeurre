from django.test import TestCase, RequestFactory, Client
from django.contrib.auth.models import User
# from accounts.forms import UserRegisterForm, UserLoginForm
from accounts.views import *


class ProductsTest(TestCase):

    def setUp(self):
        self.request = RequestFactory()
        self.user = User.objects.create_user(username='test_username',
                                             email='test@test.com',
                                             password='testpassword')

    # request.method == 'POST'
    # request.POST = {'username': 'test_username',
    #                 'email': 'test@test.com',
    #                 'password': 'testpassword'}
