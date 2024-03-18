from django.db import models
from eccomerce.base.models_base import Base
from order.models import Order

class ShippingAddress(models.Model):
    order = models.OneToOneField(
        Order, 
        on_delete=models.CASCADE, 
        null=True, 
        blank=True
    )
    address = models.CharField(
        max_length=250, 
        blank=True
    )
    city = models.CharField(
        max_length=100, 
        blank=True
    )
    postal_code = models.CharField(
        max_length=100, 
        blank=True
    )
