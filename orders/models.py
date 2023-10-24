from django.contrib.auth.models import User
from django.db import models

from product.models import Product


class OrderCart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True)
    cart_item = models.BooleanField(default=False)
    wishlist_item = models.BooleanField(default=False)
    quantity = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.product.title

