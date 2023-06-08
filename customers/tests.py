from django.test import TestCase

from django.contrib.auth.models import User
from customers.models import Customer


class CustomerTestModel(TestCase):
    
    def test_create_customer(self):        
        initial_user = User.objects.create(username="Testing", email="testing@testing.com")       
        Customer.objects.create(customer_id=initial_user.id)
    
    def test_update_customer(self):                    
        Customer.objects.update(balance=200)