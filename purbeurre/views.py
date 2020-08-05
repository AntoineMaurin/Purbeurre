from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from purbeurre.database_search import DatabaseSearch
from purbeurre.models import Product

import logging


logger = logging.getLogger(__name__)

def search(request):
    """This method sends the user search to the DatabaseSearch class,
    then calls the get_substitutes_per_category() methos on its instance,
    and returns the categories concerned and the best products within them
    to the results template, if the search is longer than 1 letter."""
    if len(request.GET.get('user_search')) > 1:
        user_search = request.GET.get('user_search')

        logger.info('New search', exc_info=True, extra={
        # Optionally pass a request and we'll grab any information we can
        'request': request,
        })

        dbs = DatabaseSearch()
        subs_per_category = dbs.get_substitutes_per_category(user_search)

        request.session['search_url'] = (request.path +
                                        '?' + request.META['QUERY_STRING'])

        context = {'user_search': user_search,
                   'subs_per_category': subs_per_category}

        return render(request, "results.html", context)
    else:
        return render(request, "home.html")


def productpage(request, id):
    product = Product.objects.get(id=id)
    return render(request, "product_page.html", {'product': product})


def homepage(request):
    return render(request, "home.html")


def legaldisclaimerpage(request):
    return render(request, "legal_disclaimer.html")


@login_required
def accountpage(request):
    return render(request, "my_account.html")
