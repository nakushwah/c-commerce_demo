from django.contrib import admin
from .models import User, Vendor, Customer
# Register your models here.

admin.site.register(Vendor)
admin.site.register(User)
admin.site.register(Customer)