from django.db import models

from customers.models import Customer
from acme_store.abstracts import BaseModel
from catalogs.models import OperationType
from products.models import Product


class Operation(BaseModel):
    operation = models.IntegerField(primary_key=True, verbose_name='Id operation')
    customer = models.ForeignKey(Customer, verbose_name='Customer', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, verbose_name='Product', on_delete=models.CASCADE)
    quantity = models.IntegerField(verbose_name='Quantity', default=0, null=False)
    price = models.DecimalField(verbose_name='Price', default=0, null=False, max_digits=8, decimal_places=4)
    operation_type = models.ForeignKey(OperationType, verbose_name='Operation Type', on_delete=models.CASCADE)
    
    def __str__(self):
        return self.operation
    
    class Meta:
        verbose_name = 'Operation register'
        verbose_name_plural = 'Operations register'
        
    