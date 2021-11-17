import uuid
from django.db import models
from accounts.models import User
from products.models import Product

from django.utils.timezone import now


class CartBaseModel(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, blank=False)
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE, blank=False, editable=False)
    date_of_add = models.DateTimeField(default=now())


class UserCart(CartBaseModel):
    quantity = models.PositiveIntegerField(default=1)
    cart_price = models.PositiveIntegerField(default=00)


class Wishlist(CartBaseModel):

    def __str__(self):
        return self.pk
