from django.db import models

from acme_store.abstracts import BaseModel

# Create your models here.
class Category(BaseModel):
    name = models.CharField(verbose_name='Name', blank=False, max_length=128)    
    description = models.TextField(verbose_name='Description', default='', max_length=2048)
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    
class OperationType(BaseModel):
    name = models.CharField(verbose_name='Type of transaction', blank=False, default='', max_length=128)
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Type of Transaction'
        verbose_name_plural = 'Types of Transactions'
