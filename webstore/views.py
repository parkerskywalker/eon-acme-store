from typing import Any, Dict
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, FormView, TemplateView
from django.urls import reverse_lazy

from django.contrib.auth.models import User
from products.models import Product
from balances.models import Operation
from customers.models import Customer

from .forms import OperationForm

# Create your views here.
class Items(LoginRequiredMixin, ListView):
    login_url = reverse_lazy('login:login')
    model = Product
    template_name = 'templates/webstore/items.html'
    
    #def get(self, request):        
    #    return HttpResponse('¡Has iniciado sesión y puedes ver esta página!')
    
class ShoppingCart(LoginRequiredMixin, FormView):
    form_class = OperationForm
    template_name = 'templates/webstore/shoppingcart.html'
    success_url = reverse_lazy('webstore:index')
    
    def get_product(self):
        return Product.objects.get(id=self.kwargs["product_id"])
    
    def get_initial(self):
        product = self.get_product()
        initial = super().get_initial()
        initial['customer']=self.request.user.customer.id
        initial['product']=product
        initial['quantity']=1
        initial['price']=product.price
        return initial

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(**kwargs)                
        context.update({
            'product':self.get_product,
        })        
        return context
    
    
