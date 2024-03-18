from django.db import models
from eccomerce.base.models_base import Base


class ProductCategory(Base):
    category_name=models.CharField(
        null=False,
        blank=False,
        max_length=256
    )

    
class Product(Base):
    product_name=models.CharField(
        null=False,
        blank=False,
        max_length=256
    )
    product_description=models.TextField(
        max_length=700,
        null=False,
        blank=False
    )
    product_available=models.BooleanField(
        default=True
    )
    product_price=models.DecimalField(
        max_digits=10,
        decimal_places=2,
        null=False, 
        blank=False
    )
    product_category=models.ForeignKey(
        ProductCategory,
        null=True,
        blank=False,
        on_delete=models.CASCADE
    )
    product_quantity=models.IntegerField(
        null=False,
        blank=False,
        default=0
    )
   
    
class ProductImages(Base):
    product_image=models.ImageField(
        upload_to=None, 
        height_field=None, 
        width_field=None, 
        max_length=None
    )
    product=models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        null=False,
        blank=False
    )
    product_image_number=models.PositiveSmallIntegerField(
        null=False,
        blank=False,
        default=1
    )


class ProductFeatures(Base):
    features=models.CharField(
        max_length=50,
        null=False,
        blank=False
    )
    features_product=models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        null=False
    )
  

