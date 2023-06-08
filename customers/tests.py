from django.test import TestCase

from django.contrib.auth.models import User
from customers.models import Customer


class CustomerTestModel(TestCase):
    
    def test_create_customer(self):    
        initial_count = Customer.objects.count() 
        initial_user = User.objects.create(username="Testing", email="testing@testing.com")       
        new_product = Customer.objects.create(customer_id=initial_user.id)
    
    def test_update_customer(self):                    
        new_product = Customer.objects.update(balance=200)

        