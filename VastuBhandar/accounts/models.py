"""creating account app's  models which contains model
    User :- which contains user basic and authenticate info
    Address:- this is the base class for creating vendor , and customer

"""

import uuid
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.timezone import now
from django.db.models.signals import post_save
from django.dispatch import receiver
from .TokenGenrator import token_create
from .task import send_mail_for_verification_link


class User(AbstractUser):
    """
        user model using AbstractUser adding some extra fields in basic user model
    """
    ROLE_CHOICES = (
        ("Vendor", "Vendor"),
        ("User", "User"),
    )
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user_type = models.CharField(choices=ROLE_CHOICES, default="Vendor", max_length=50)
    contact = models.PositiveIntegerField(max_length=10,
                                          verbose_name="Mobile Number", null=True)
    contact2 = models.PositiveIntegerField(max_length=10,
                                           verbose_name="Alternate NUmber", null=True)
    is_verified = models.BooleanField(default=False)
    created_date = models.DateTimeField(default=now())
    updated_date = models.DateTimeField(default=now())


class Address(models.Model):
    """
     this class is creating as baseclass for account app's other model
     customer , vendor
    """
    cnt_choices = (("INDIA", "INDIA"), ("USA", "USA"))
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    country = models.CharField(choices=cnt_choices, max_length=10)
    address = models.TextField(max_length=500)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    zipcode = models.PositiveIntegerField(max_length=5, null=True)
    created_date = models.DateTimeField(default=now())
    updated_date = models.DateTimeField(default=now())


class Customer(Address):
    """
    A class for  creating user as customer inheriting the Address base class
    added one more field (landmark)
    """
    landmark = models.TextField()


class Vendor(Address):
    """ creating class model for vendor (user) using the Address base class
    added one more field (shop_name)
    """
    shop_name = models.CharField(max_length=250)


@receiver(post_save, sender=User)
def create_vendor_or_customer(sender, instance, created, **kwargs):
    """
    Using post signal for creating vendor's and customer's objects
    """
    if created and instance.user_type == "Vendor":
        obj = Vendor.objects.create(user_id=instance)
        obj.save()
        send_verification_link(user=instance)
    elif created and instance.user_type == "Customer":
        obj = Customer.objects.create(user_id=instance)
        obj.save()
        send_verification_link(user=instance)
    else:
        pass


def send_verification_link(user):
    token = token_create(user)
    """ calling task for sending the mail"""
    send_mail_for_verification_link.delay(user.email, user.username, token)
