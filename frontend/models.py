from django.conf import settings
from django.db import models

from users.forms import User


class Product(models.Model):
    productname = models.CharField(max_length=200)
    price = models.IntegerField()
    description = models.TextField()
    image = models.ImageField(upload_to='images/')
    author = models.ForeignKey(User,
                               null=True,
                               on_delete=models.CASCADE,
                               related_name='products',
                               )
    slug = models.SlugField(null=True, blank=True, help_text="Product slug field", db_column="product_slug",
                                    verbose_name="slug product", error_messages={"required": "Enter the slug field"},
                                    unique=True, )
