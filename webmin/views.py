from django.contrib.auth.mixins import LoginRequiredMixin

from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from customers.models import Customer
from products.models import Product


""" SECTION PRODUCT """
class ProductDetail(DetailView, LoginRequiredMixin):
    model = Product
    template_name = 'templates/webmin/products/product_detail.html'
    context_object_name = 'product'

class ProductCreate(CreateView, LoginRequiredMixin):
    model = Product
    fields = ['name', 'description', 'price', 'category', 'stock']
    template_name = 'templates/webmin/products/product_create.html'    
    success_url = reverse_lazy('webmin:product_list')
    
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            'title':'Form Product Create'
        })
        return context

class ProductList(ListView, LoginRequiredMixin):
    model = Product
    template_name = 'templates/webmin/products/product_list.html'
    context_object_name = 'products'
        
class ProductUpdate(UpdateView, LoginRequiredMixin):
    model = Product
    fields = ['name', 'description', 'price', 'category', 'stock']
    template_name = 'templates/webmin/products/product_update.html'
    context_object_name = 'product'
    success_url = reverse_lazy('webmin:product_list')

class ProductDelete(DeleteView, LoginRequiredMixin):
    model = Product
    template_name = 'templates/webmin/products/product_delete.html'
    context_object_name = 'product'
    success_url = reverse_lazy('webmin:product_list')
