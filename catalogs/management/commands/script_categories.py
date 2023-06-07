from django.core.management.base import BaseCommand, CommandError
from catalogs.models import Category, OperationType

class Command(BaseCommand):
    help = "Add categories"
    
    def handle(self, *args, **options):
        categories = [
            {'name': 'Abarrotes', 'description': 'Department abarrotes'},
            {'name': 'Farmacia', 'description': 'Department farmacia'},
            {'name': 'Electrónica', 'description': 'Department electrónica'},
        ]
        
        operations = [
            {'name':'Compra'},
            {'name':'Venta'}
        ]
        
        for cat in categories:            
            new_category = Category()
            new_category.name = cat["name"]
            new_category.description = cat["description"]
            new_category.save()
            
            print("Categoria {} creada exitosamente! ".format(cat["name"]))
            
        for ope in operations:
            new_operation = OperationType()
            new_operation.name = ope["name"]
            new_operation.save()
            
            print("Tipo operacion: {} creada exitosamente! ".format(ope["name"]))