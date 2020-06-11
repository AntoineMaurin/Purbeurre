from purbeurre.models import Product, Category
from django.db.models import Q
from collections import Counter


class DatabaseSearch:

    def get_substitutes_per_category(self, search):
        cat_subs_list = []
        categories = self.get_categories_from_search(search)
        print('categories : ', categories)
        if categories == None:
            return None
        else:
            for i, cat in enumerate(categories):
                cat_subs_list.append({cat : []})
                rq = Product.objects.filter(category__name=cat).order_by('nutriscore')[:6]
                for r in rq:
                    cat_subs_list[i][cat].append(r)

            for elt in cat_subs_list:
                print('\ndict : ', elt)
            return cat_subs_list

    def get_categories_from_search(self, search):

        products = Product.objects.filter(Q(name__startswith=search.lower())
                                          | Q(name__contains=search.lower()))

        return self.keep_only_real_categories(products)


    def keep_only_real_categories(self, products):
        categories_list = []

        for product in products:
            categories_list.append(product.category.name)

        if len(categories_list) == 0:
            return None
            
        greatest = max(Counter(categories_list).values())

        final_list = []
        for k, v in Counter(categories_list).items():
            if v < greatest*0.01:
                print(v, k , 'inférieurs à 1% de', greatest)
            else:
                print(v, k)
                final_list.append(k)

        return final_list
