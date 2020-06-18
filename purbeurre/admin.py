from django.contrib import admin

# Register your models here.
from purbeurre.models import Category, Product
from favourites.models import Favourite

admin.site.register(Category)
admin.site.register(Product)
admin.site.register(Favourite)
