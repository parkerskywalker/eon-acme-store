from django.core.management.base import BaseCommand, CommandError
from django.contrib.auth.models import User

from customers.models import Customer

class Command(BaseCommand):
    help = "Add customers"
    
    def handle(self, *args, **options):        
            
        usersLst = [
            {'username': 'superadmin', 'password': 'acme12345', 'email':'parker_1978@hotmail.com', 'is_superuser':True, 'first_name':'Jose', 'last_name':'Carranza'},
            {'username': 'customer1', 'password': 'contrasena1', 'email':'customer@one.com', 'is_superuser':False, 'first_name':'customer', 'last_name':'one'},
            {'username': 'customer2', 'password': 'contrasena2', 'email':'customer@two.com', 'is_superuser':False, 'first_name':'customer', 'last_name':'two'},
            {'username': 'customer3', 'password': 'contrasena3', 'email':'customer@three.com', 'is_superuser':False, 'first_name':'customer', 'last_name':'three'},
            {'username': 'customer4', 'password': 'contrasena4', 'email':'customer@three.com', 'is_superuser':False, 'first_name':'customer', 'last_name':'four'},
        ]
                
        for customer in usersLst:
            new_user = User.objects.create_user(username=customer['username'], password=customer['password'], email=customer['email'], first_name=customer['first_name'], last_name=customer['last_name'])
        
            customer = Customer()
            customer.customer_id=new_user.id
            customer.save()
            
            print("Usuario {} creado exitosamente.".format(new_user.username))