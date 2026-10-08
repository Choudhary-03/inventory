from django.db import models
from .product import Product


class Stock(models.Model):
    product= models.OneToOneField(Product, on_delete= models.CASCADE, related_name='stock')
    quantity= models.PositiveIntegerField(default=0)
    
    def __str__(self):
        return f'{self.product.name}-{self.quantity}'