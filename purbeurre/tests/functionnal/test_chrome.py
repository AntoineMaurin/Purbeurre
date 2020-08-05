from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from purbeurre.models import Product, Category


class PurbeurreChromeTest(StaticLiveServerTestCase):
    def setUp(self):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument("--headless")
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--disable-dev-shm-usage")
        chrome_options.add_argument("--disable-gpu")
        chrome_options.add_argument("--window-size=1920,1080")

        self.browser = webdriver.Chrome('purbeurre/tests/functionnal/'
                                        'chromedriver',
                                        chrome_options=chrome_options)

    def tearDown(self):
        self.browser.close()

    def create_product(self):
        category = Category.objects.create(name='pates a tartiner aux nois'
                                                'ettes et au cacao')

        Product.objects.create(
            name='Choc! Noisette cacao et lait - 220 g',
            nutriscore='b',
            url='https://fr.openfoodfacts.org/produit/3770012968298/'
                'choc-noisette-cacao-et-lait/',
            image_url='https://static.openfoodfacts.org/images/products/377/'
                      '001/296/8298/front_fr.3.full.jpg',
            fat_100g=6.6,
            saturated_fat_100g=0.68,
            sugars_100g=6.1,
            salt_100g=0.13,
            category=category
            )

    def create_d_and_e_nutriscores_products(self):
        category = Category.objects.create(name='pates a tartiner aux nois'
                                                'ettes et au cacao')

        Product.objects.create(
            name='Nutella - Ferrero - 750g',
            nutriscore='e',
            url='https://fr.openfoodfacts.org/produit/4008400404127/'
                'nutella-ferrero',
            image_url='https://static.openfoodfacts.org/images/products/400/'
                      '840/040/4127/front_fr.49.400.jpg',
            fat_100g=30.9,
            saturated_fat_100g=10.6,
            sugars_100g=56.3,
            salt_100g=0.107,
            category=category
            )

        Product.objects.create(
            name='NuPâte à tartiner - U - 1 kg',
            nutriscore='d',
            url='https://fr.openfoodfacts.org/produit/3256227557187/'
                'pate-a-tartiner-u',
            image_url='https://static.openfoodfacts.org/images/products/325/'
                      '622/755/7187/front_fr.23.400.jpg',
            fat_100g=29,
            saturated_fat_100g=4.8,
            sugars_100g=57,
            salt_100g=0.18,
            category=category
            )

    def test_basic_user_cycle(self):
        """This test starts by creating a test account with the register form,
        then submits and verifies that the user is redirected to the login
        page in case of success. Once on the login page, enters the right
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

        self.browser.find_element_by_class_name("btn-primary").click()

        username = self.browser.find_element_by_name("username")
        password = self.browser.find_element_by_name("password")

        username.send_keys("thetest@test.com")
        password.send_keys("testpassword")

        self.browser.find_element_by_class_name("btn-primary").click()

        self.assertEquals(
            self.browser.current_url[:-1],
            self.live_server_url
            )

        self.create_product()

        user_search = self.browser.find_element_by_id("user_search")

        user_search.send_keys("cacao")

        self.browser.find_element_by_class_name("btn-primary").click()

        self.assertEquals(
            self.browser.current_url,
            self.live_server_url + '/results?user_search=cacao'
            )

        self.browser.find_element_by_tag_name('h6').click()

        carrot_icon = self.browser.find_element_by_xpath('//a[contains'
                                                         '(@href,"/myfood")]')

        carrot_icon.click()

        self.assertEquals(
            self.browser.current_url,
            self.live_server_url + '/myfood'
            )

        favourite = self.browser.find_element_by_tag_name('p')

        self.assertEquals(
            favourite.text,
            'Choc! noisette cacao et lait - 2...'
            )

    def test_results_nutriscores_better_than_d(self):

        self.create_d_and_e_nutriscores_products()

        self.browser.get(self.live_server_url)

        user_search = self.browser.find_element_by_id("user_search")

        user_search.send_keys("Nutella")

        self.browser.find_element_by_class_name("btn-primary").click()

        try:
            self.browser.find_element_by_class_name("food-pic-container")
            not_found = False
        except(NoSuchElementException):
            not_found = True

        self.assertTrue(not_found)

    def test_save_button_from_product_page(self):

        self.browser.get(self.live_server_url + '/accounts/register')
        self.assertEquals(
            self.browser.current_url,
            self.live_server_url + '/accounts/register'
            )
        email = self.browser.find_element_by_name("email")
        pw1 = self.browser.find_element_by_name("pw1")
        pw2 = self.browser.find_element_by_name("pw2")
        email.send_keys("testsavebutton@test.com")
        pw1.send_keys("testpassword")
        pw2.send_keys("testpassword")

        self.browser.find_element_by_class_name("btn-primary").click()

        username = self.browser.find_element_by_name("username")
        password = self.browser.find_element_by_name("password")

        username.send_keys("testsavebutton@test.com")
        password.send_keys("testpassword")

        self.browser.find_element_by_class_name("btn-primary").click()

        self.create_product()

        user_search = self.browser.find_element_by_id("user_search")

        user_search.send_keys("cacao")

        self.browser.find_element_by_class_name("btn-primary").click()

        self.assertEquals(
            self.browser.current_url,
            self.live_server_url + '/results?user_search=cacao'
            )

        self.browser.find_element_by_class_name('food-pic-container').click()

        self.assertEquals(
            self.browser.current_url,
            self.live_server_url + '/product/49420'
            )

        self.browser.find_element_by_xpath('//a[contains'
                                           '(@href,"/save/49420")]').click()

        carrot_icon = self.browser.find_element_by_xpath('//a[contains'
                                                         '(@href,"/myfood")]')

        carrot_icon.click()

        self.assertEquals(
            self.browser.current_url,
            self.live_server_url + '/myfood'
            )

        favourite = self.browser.find_element_by_tag_name('p')

        self.assertEquals(
            favourite.text,
            'Choc! noisette cacao et lait - 2...'
            )

    def test_initial_search_after_login(self):

        self.browser.get(self.live_server_url + '/accounts/register')
        self.assertEquals(
            self.browser.current_url,
            self.live_server_url + '/accounts/register'
            )
        email = self.browser.find_element_by_name("email")
        pw1 = self.browser.find_element_by_name("pw1")
        pw2 = self.browser.find_element_by_name("pw2")
        email.send_keys("testredirection@test.com")
        pw1.send_keys("testpassword")
        pw2.send_keys("testpassword")

        self.browser.find_element_by_class_name("btn-primary").click()

        self.create_product()

        self.browser.get(self.live_server_url)

        user_search = self.browser.find_element_by_id("user_search")

        user_search.send_keys("cacao")

        self.browser.find_element_by_class_name("btn-primary").click()

        self.browser.find_element_by_tag_name('h6').click()

        self.assertEquals(
            self.browser.current_url,
            self.live_server_url + '/accounts/login?next=/save/49417'
            )

        username = self.browser.find_element_by_name("username")
        password = self.browser.find_element_by_name("password")

        username.send_keys("testredirection@test.com")
        password.send_keys("testpassword")

        self.browser.find_element_by_class_name("btn-primary").click()

        self.assertEquals(
            self.browser.current_url,
            self.live_server_url + '/results?user_search=cacao'
            )
