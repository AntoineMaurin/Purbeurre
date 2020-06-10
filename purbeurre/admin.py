from django.contrib import admin

# Register your models here.
from purbeurre.models import Category, Product, Search

admin.site.register(Category)
admin.site.register(Product)
admin.site.register(Search)
