from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from purbeurre.database_search import DatabaseSearch
from purbeurre.models import Product, Category, Favourite
from django.contrib.auth.models import User
from accounts import views
from django.http import HttpResponse
from django.contrib import messages

def search(request):
    if len(request.GET.get('user_search')) > 1:
        user_search = request.GET.get('user_search')
        dbs = DatabaseSearch()
        subs_per_category = dbs.get_substitutes_per_category(user_search)

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

@login_required
def save(request, id):
    user_mail = request.session['user_mail']
    user = User.objects.get(email=user_mail)

    product = Product.objects.get(id=id)

    if not Favourite.objects.filter(user=user, product=product).exists():
        Favourite.objects.create(user=user, product=product)
        messages.info(request, "Aliment ajouté à votre liste !")
    else:
        messages.info(request, "Ce produit est déjà dans votre liste !")

    return redirect(request.META['HTTP_REFERER'])

@login_required
def remove(request, id):
    user_mail = request.session['user_mail']
    user = User.objects.get(email=user_mail)

    product = Product.objects.get(id=id)

    Favourite.objects.filter(user=user, product=product).delete()

    messages.info(request, "Produit supprimé !")

    return redirect(request.META['HTTP_REFERER'])


@login_required
def myfoodpage(request):
    user_mail = request.session['user_mail']
    user = User.objects.get(email=user_mail)

    favs = Favourite.objects.filter(user=user)

    favourites = []

    for fav in favs:
        favourites.append(fav.product)

    context = {'products': favourites}

    return render(request, "my_food.html", context)

@login_required
def accountpage(request):
    return render(request, "my_account.html")
