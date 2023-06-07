from django.db import models

from acme_store.abstracts import BaseModel

from catalogs.models import Category

# Create your models here.
class Product(BaseModel):
    name = models.CharField(verbose_name='Name', blank=False, default='', max_length=128)
    description = models.TextField(verbose_name='Description')
    price = models.DecimalField(verbose_name='Price', null=False, max_digits=8, decimal_places=2)
    category = models.ForeignKey(Category, verbose_name='Category', on_delete=models.CASCADE)
    stock = models.IntegerField(verbose_name='Stock', null=False, default=0)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "Product"
        verbose_name_plural = "Products"
        
    @property
    def available(self):
        if self.stock > 0:
            return True
        return False    
    