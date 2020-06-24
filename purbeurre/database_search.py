from purbeurre.models import Product
from django.db.models import Q
from collections import Counter


class DatabaseSearch:

    def get_substitutes_per_category(self, search):
        cat_subs_list = []
        categories = self.get_categories_from_search(search)

        if categories is None:
            return None
        else:
            for i, cat in enumerate(categories.keys()):
                cat_subs_list.append({cat: []})
                rq = Product.objects.filter(category__name=cat).order_by(
                    'nutriscore'
                    )[:6]
                for r in rq:
                    cat_subs_list[i][cat].append(r)

            return cat_subs_list

    def get_categories_from_search(self, search):

        products = Product.objects.filter(Q(name__startswith=search.lower())
                                          | Q(name__contains=search.lower()))

        return self.keep_only_real_categories(products)

    def keep_only_real_categories(self, products):
        categories_list = []

        # For each product, adds its category name to a list
        for product in products:
            categories_list.append(product.category.name)

        if len(categories_list) == 0:
            return None

        # Gets the category the most present
        greatest = max(Counter(categories_list).values())

        keys_to_del = []

        # Builds and sorts a dict from the category the most present
        # to the least
        dict = Counter(categories_list)
        the_dict = {k: v for k, v in sorted(dict.items(),
                                            key=lambda item: item[1],
                                            reverse=True)}
        # Checks which categories are too few
        for k, v in the_dict.items():
            if v < greatest*0.1:
                keys_to_del.append(k)

        # Removes them
        for key in keys_to_del:
            del(the_dict[key])

        return the_dict
