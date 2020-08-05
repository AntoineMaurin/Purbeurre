from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from purbeurre.models import Product
from favourites.models import Favourite
from django.contrib import messages


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
