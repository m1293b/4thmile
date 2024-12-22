from django.contrib import admin
from .models import ShippingAddress, ShippingMethod

# Register your models here.

admin.site.register(ShippingAddress)
admin.site.register(ShippingMethod)