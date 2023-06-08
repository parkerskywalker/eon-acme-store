from django.core.management.base import BaseCommand, CommandError

from products.models import Product
from catalogs.models import Category

class Command(BaseCommand):
    help = "Add categories"
    
    def handle(self, *args, **options):
        
        products = [            
            {'name':'Manzana', 'description':'manzana', 'price':'2.00', 'category':'','stock':'5'},
            {'name':'Pera', 'description':'Pera', 'price':'3.00', 'category':'','stock':'10'},
            {'name':'Uva', 'description':'Uva', 'price':'12.00', 'category':'','stock':'13'},
        ]
        
        for product in products:
            cat = Category.objects.all().first()
            data = Product.objects.create(name=product['name'], description=product['description'], price=product['price'], category=cat, stock=product['stock'])
            print("Producto {} creado exitosamente.".format(data.name))