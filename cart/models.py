from django.db import models
from eccomerce.base.models_base import Base
from products.models import Product

class Cart(Base):
    product=models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        null=False,
        blank=False
    )
     
    
