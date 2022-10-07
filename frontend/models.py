from django.conf import settings
from django.db import models

from users.forms import User


class Product(models.Model):
    productname = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    description = models.TextField()
    image = models.ImageField(upload_to='images/')
    author = models.ForeignKey(User,
                               null=True,
                               on_delete=models.CASCADE,
                               related_name='products',
                               )
