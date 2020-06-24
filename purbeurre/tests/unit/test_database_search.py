from django.test import TestCase
from purbeurre.database_search import DatabaseSearch


class DatabaseSearchTest(TestCase):

    fixtures = ['purbeurre/fixtures/dump.json']

    def setUp(self):
        self.dbs = DatabaseSearch()

    def test_simple_category_search(self):
        subs_per_category = self.dbs.get_substitutes_per_category('Nutella')
        assert (
            'pates a tartiner aux noisettes et au cacao' in
            subs_per_category[0].keys()
            )

    def test_multiple_categories_search(self):
        supposed_categories = ['biscuits sables',
                               'pates a tartiner aux noisettes et au cacao',
                               'liegeois']

        subs_per_category = self.dbs.get_substitutes_per_category('chocolat')

        for i in range(len(subs_per_category)):
            assert supposed_categories[i] in subs_per_category[i].keys()

    def test_search_gives_no_results(self):
        result = self.dbs.get_substitutes_per_category('fsfklhsdflqj')
        assert result is None
