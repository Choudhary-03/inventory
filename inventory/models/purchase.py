from django.db import models
from .product import Product
from .supplier import Supplier

class Purchase(models.Model):
    product= models.ForeignKey(Product, on_delete=models.CASCADE)
    supplier= models.ForeignKey(Supplier, on_delete= models.CASCADE)
    quantity= models.PositiveIntegerField()
    purchase_date= models.DateTimeField(auto_now_add=True)
