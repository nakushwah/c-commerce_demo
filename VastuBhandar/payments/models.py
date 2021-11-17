import uuid
from django.db import models
from WishlistCart.models import UserCart
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils.timezone import now


# Create your models here.
class PaymentCheckOut(models.Model):
    STATUS_CHOICE = (
        ("unpaid", "unpaid"),
        ("paid", "paid"),
        ("in_process", "in_process"),
        ("initiate", "initiate"))

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    cart = models.ForeignKey(UserCart, on_delete=models.CASCADE, unique=True)
    amount = models.PositiveIntegerField()
    payment_id = models.CharField(max_length=500)
    status = models.CharField(choices=STATUS_CHOICE, default="initiate", max_length=500,)
    created_at = models.DateTimeField(default=now(), editable=False)
    updated_at = models.DateTimeField(default=now())


class OrderHistory(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    Payment_id = models.ForeignKey(PaymentCheckOut, on_delete=models.CASCADE)
    purchased_on = models.DateTimeField(default=now(), editable=False)


@receiver(post_save, sender=PaymentCheckOut)
def create_order_history(sender, instance, created, **kwargs):
    """ after PaymentCheckOut PaymentCheckOut then we are creating
     a order history by the instance of PaymentCheckOut"""
    if created:
        obj = OrderHistory.objects.create(Payment_id=instance)
        obj.save()
