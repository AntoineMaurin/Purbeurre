from django.db import models
from django.contrib.auth.models import User
from purbeurre.models import Product


class Favourite(models.Model):
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    product = models.ForeignKey(Product, on_delete=models.PROTECT)

    def __str__(self):
        return self.user.email
