from django.db import models
from eccomerce.base.models_base import Base
from products.models import Product


class Order(Base):
    order_products=models.ManyToManyField(
        to=Product, 
        related_name="products"
    )    
    total_price=models.DecimalField(
        max_digits=10,
        decimal_places=2,
        null=False, 
        blank=False
    )
    is_delivered = models.BooleanField(
        default=False
    )
    delivered_at = models.DateTimeField(
        auto_now_add=False, 
        null=True, 
        blank=True
    )