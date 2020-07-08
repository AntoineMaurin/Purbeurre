from django.db import models


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
    category = models.ForeignKey(Category, on_delete=models.PROTECT)

    def __str__(self):
        return self.name
