from django.contrib import admin
from .models import PaymentCheckOut, OrderHistory

# Register your models here.

admin.site.register(PaymentCheckOut)
admin.site.register(OrderHistory)