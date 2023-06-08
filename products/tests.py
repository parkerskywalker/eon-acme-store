from django.test import TestCase

from catalogs.models import Category
from products.models import Product


class ProductTestModel(TestCase):
    
    def test_create_product(self):
    
        initial_count = Product.objects.count()        

        for cat in Category.objects.filter(id=1):
            category = Category.objects.get(id=cat.id)

            new_product = Product.objects.create(name='Product 2', price=20, category=category)
            new_count = Product.objects.count()
            self.assertEqual(new_count, initial_count + 1)
            self.assertEqual(new_product.name, 'Product 2')
            self.assertEqual(new_product.price, 20)

    
    def test_read_product(self):
        for items in Product.objects.all():
            product = Product.objects.filter(id=items.id)            
            self.assertEqual(product.price, 10)

    

    def test_update_product(self):
        for items in Product.objects.all():
            product = Product.objects.id(id=items.id)
            product.price = 15.00
            product.save()
            updated_product = Product.objects.get(name='Product 1')
            self.assertEqual(updated_product.price, 15)

    
    def test_delete_product(self):
        for items in Product.objects.all():
            initial_count = Product.objects.filter(id=items.id)
            self.product.delete()
            new_count = Product.objects.count()
            self.assertEqual(new_count, initial_count - 1)
    

