from django.db import models

from django.contrib.auth.models import User

class Category(models.Model):
    name = models.CharField(max_length=150)

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=150)
    nutriscore = models.CharField(max_length=1)
    url = models.URLField()
    image_url = models.URLField(default=None)
    fat_100g = models.FloatField(default=None)
    saturated_fat_100g = models.FloatField(default=None)
    sugars_100g = models.FloatField(default=None)
    salt_100g = models.FloatField(default=None)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.name

class Search(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='product')
    substitute = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='substitute')

    def __str__(self):
        return self.user.email
