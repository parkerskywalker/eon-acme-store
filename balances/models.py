from django.db import models

from customers.models import Customer
from acme_store.abstracts import BaseModel, BaseModelBalance
from catalogs.models import OperationType
from products.models import Product


class Operation(BaseModelBalance):
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

    def save(self, *args, **kwargs):
        product = self.product
        quantity = self.quantity        
        
        self.update_stock(self.product, self.quantity, self.operation_type)
        
        super().save(*args, **kwargs)   
        
    
    def update_stock(self, product, quantity, operation_type):
    
        if 'sale' in operation_type.name.lower():
            result = product.retrieve_stock + quantity    
        elif 'purchase' in operation_type.name.lower():
            result = product.retrieve_stock - quantity
        
        update_product = Product.objects.filter(id=product.id).update(stock=result)
        
        return     
        
        