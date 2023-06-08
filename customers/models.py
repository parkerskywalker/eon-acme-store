from django.contrib.auth.models import User
from django.db import models

#from balances.models import Operation

# Create your models here.
BALANCE_INITIAL = 1000


class Customer(models.Model):
    customer = models.OneToOneField(User, on_delete=models.CASCADE)
    balance = models.DecimalField(verbose_name='Balance initial', null=False, default=BALANCE_INITIAL, max_digits=8, decimal_places=4)
    
    class Meta:
        verbose_name = 'Customer'
        verbose_name_plural = 'Customers'
                    
    @property
    def get_sales(self):            
        price = 0
        for sale in self.operation_set.filter(operation_type=2):        
            price += sale.price
            
        return price
    
    @property
    def get_purchases(self):        
        price = 0
        for purchase in self.operation_set.filter(operation_type=1):
            price += purchase.price
        return price
    
    @property
    def get_account_statement(self):        
        return (self.balance + self.get_sales) - self.get_purchases
        