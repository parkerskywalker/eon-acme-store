from django.core.management.base import BaseCommand, CommandError
from products.models import Product

class Command(BaseCommand):
    help = "Add categories"
    
    def handle(self, *args, **options):
        
        products = [            
            {'name':'', 'description':'', 'price':'', 'category':'','stock':'',}
        ]
        
        
        