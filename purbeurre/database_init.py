import requests
import json

from purbeurre.models import Product, Category


class DatabaseInit:
    """This class's job is to fill the database with a given file of urls of
    openfoodfacts categories of products."""
    def __init__(self, file):
        urls_file = open(file, "r")
        self.urls = [(line.strip()) for line in urls_file.readlines()]
        print(self.urls)

    def get_category_from_url(self, url):
        end_url = url.split("/")[4]
        current_category = end_url.split(".")[0].replace("-", " ")
        return current_category

    def get_products(self, url):
        try:
            response = requests.get(url, headers={'User-Agent':
                                                  "Purbeurre - "
                                                  "windows/mac - "
                                                  "Version 1.0"})
            assert response.status_code < 400
        except AssertionError:
            print("Bad status code")
        else:
            pass

        json_response = json.loads(response.text)
        return json_response

    def request(self):
        """For every url in the file, this method adds the category itself
        in database, and loops throught the pages to get each product and add
        it in database."""
        for url in self.urls:
            category_name = self.get_category_from_url(url)
            # print(category_name)
            if not Category.objects.filter(name=category_name).exists():
                Category.objects.create(name=category_name)

            category = Category.objects.get(name=category_name)

            i = 0
            while True:
                i += 1
                incremented_url = url[:-5] + '/' + str(i) + '.json'
                print('url : ', incremented_url[:-5])

                json_response = self.get_products(incremented_url)

                if json_response["products"] == []:
                    break

                for elt in json_response["products"]:
                    product = self.build_product(elt)
                    if not Product.objects.filter(url=product.url).exists():
                        product.category = category
                        product.save()

    def build_product(self, dict):
        name = self.get_basic_data('product_name_fr', dict)
        nutri = self.get_basic_data('nutrition_grade_fr', dict)
        image_front_url = self.get_basic_data('image_front_url', dict)
        url_off = self.get_basic_data('url', dict)
        sugars_100g = self.get_nutriments_data('sugars_100g', dict)
        salt_100g = self.get_nutriments_data('salt_100g', dict)
        saturated_fat_100g = self.get_nutriments_data('saturated-fat_100g',
                                                      dict)
        fat_100g = self.get_nutriments_data('fat_100g', dict)

        return Product(name=name,
                       nutriscore=nutri,
                       url=url_off,
                       image_url=image_front_url,
                       fat_100g=fat_100g,
                       saturated_fat_100g=saturated_fat_100g,
                       sugars_100g=sugars_100g,
                       salt_100g=salt_100g)

    def get_basic_data(self, key, dict):
        if key in dict:
            return dict[key].replace('\n', "").lower()
        elif key not in dict and key == 'nutrition_grade_fr':
            return "n"
        else:
            return "Nom inconnu"

    def get_nutriments_data(self, key, dict):
        if key in dict['nutriments']:
            return dict['nutriments'][key]
        else:
            return -1

    def delete_products(self):
        products = Product.objects.all()
        for product in products:
            try:
                product.delete()
            except:
                pass

        categories = Category.objects.all()
        for category in categories:
            try:
                category.delete()
            except:
                pass
