from django.test import TestCase

from catalogs.models import OperationType
from balances.models import Operation
from customers.models import Customer
from products.models import Product

class OperationTestModel(TestCase):
    
    def test_create_operation(self):
    
        initial_count = Operation.objects.count() 
        customer = Customer.objects.get(customer_id=1)              
        product = Product.objects.get(id=1)
        type = OperationType.objects.get(id=1)
        
        Operation.objects.create(operation=initial_count+1, customer=customer, product=product, quantity=3, price=20, operation_type=type)