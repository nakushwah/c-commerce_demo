import uuid
from django.db import models
from django.utils.timezone import now


# Create your models here.
class Product(models.Model):
    avl = (
        ("Coming soon", "Coming soon"),
        ("Available", "Available"),
        ("Not Available", "Not Available")
    )

    categories = (
        ("general", "general"),
        ("fashion", "fashion"),
        ("mobile", "mobile"),
        ("books", "books"),
    )
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=300, blank=False)
    details = models.TextField(blank=False)
    price = models.FloatField(blank=False)
    stocks = models.IntegerField(blank=False)
    availability = models.CharField(choices=avl, default='available', blank=False, max_length=20)
    category = models.CharField(choices=categories, default='general', blank=False, max_length=50)
    image1 = models.FileField(blank=False, help_text="Add products image here", upload_to="product/images")
    created_at = models.DateTimeField(default=now())
    updated_at = models.DateTimeField(default=now())


