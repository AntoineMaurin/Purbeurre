from selenium import webdriver
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from django.contrib.auth.models import User
import time


class PurbeurreChromeTest(StaticLiveServerTestCase):

    def setUp(self):
        self.browser = webdriver.Chrome('purbeurre/tests/functionnal/'
                                        'chromedriver.exe')

    def tearDown(self):
        self.browser.close()

    def test_user_can_register_and_login(self):
        """This test starts by creating a test account with the register form,
        then submits and verifies that the user is redirected to the login
        page in case of success. Once on the login page, enters bad credentials
        and checks is the error message is as expected. Then enters the right
        credentials and verifies that we are connected and on the home page."""

        self.browser.get(self.live_server_url + '/accounts/register')

        self.assertEquals(
            self.browser.current_url,
            self.live_server_url + '/accounts/register'
            )

        email = self.browser.find_element_by_name("email")
        pw1 = self.browser.find_element_by_name("pw1")
        pw2 = self.browser.find_element_by_name("pw2")

        email.send_keys("thetest@test.com")
        pw1.send_keys("testpassword")
        pw2.send_keys("testpassword")

        self.browser.find_element_by_name("submit").click()

        self.assertTrue(
            User.objects.filter(email='thetest@test.com').exists()
            )

        alert = self.browser.find_element_by_class_name("alert-success")

        self.assertEquals(
            alert.text,
            'Compte créé ! Bienvenue thetest@test.com'
            )

        time.sleep(2)

        username = self.browser.find_element_by_name("username")
        password = self.browser.find_element_by_name("password")

        username.send_keys("thetest@test.com")
        password.send_keys("wrongpassword")

        self.browser.find_element_by_name("submit").click()

        self.assertEquals(
            self.browser.current_url,
            self.live_server_url + '/accounts/login'
            )

        alert = self.browser.find_element_by_class_name("alert-error")
        self.assertEquals(alert.text, 'Email ou mot de passe incorrect.')

        time.sleep(2)

        username = self.browser.find_element_by_name("username")
        password = self.browser.find_element_by_name("password")

        username.send_keys("thetest@test.com")
        password.send_keys("testpassword")

        self.browser.find_element_by_name("submit").click()

        self.assertEquals(
            self.browser.current_url[:-1],
            self.live_server_url
            )

        time.sleep(5)
