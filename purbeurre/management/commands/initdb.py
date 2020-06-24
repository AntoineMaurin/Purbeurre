from django.core.management.base import BaseCommand
from purbeurre.database_init import DatabaseInit


class Command(BaseCommand):

    help = """\nUsing : python manage.py initdb <file_to_use> \n
           The file to use must contain urls of categories of products you
           want to use from OpenFoodFacts, with .json in the end,
           for example : \n
           https://fr.openfoodfacts.org/categorie/pates-a-tartiner.json
           https://fr.openfoodfacts.org/categorie/biscuits-secs.json
           https://fr.openfoodfacts.org/categorie/pizzas.json
           https://fr.openfoodfacts.org/categorie/liegeois.json
           https://fr.openfoodfacts.org/categorie/yaourts-natures.json"""

    def add_arguments(self, parser):
        parser.add_argument('urls_file')

    def handle(self, *args, **options):

        try:
            d = DatabaseInit(options['urls_file'])
            d.delete_products()
            d.request()
        except(FileNotFoundError):
            print('File not found, see the help : ', self.help)
