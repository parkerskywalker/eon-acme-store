from typing import Any, Dict
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, FormView, TemplateView
from django.urls import reverse_lazy

from django.contrib.auth.models import User
from products.models import Product
from balances.models import Operation
from customers.models import Customer

from .forms import ShoppingCartForm

# Create your views here.
class Items(LoginRequiredMixin, ListView):
    login_url = reverse_lazy('login:login')
    model = Product
    template_name = 'templates/webstore/items.html'
    
    #def get(self, request):        
    #    return HttpResponse('¡Has iniciado sesión y puedes ver esta página!')
    
class ShoppingCart(LoginRequiredMixin, FormView):
    form_class = ShoppingCartForm
    template_name = 'templates/webstore/shoppingcart.html'
    success_url = reverse_lazy('webstore:index')
    
    def get_product(self):
        return Product.objects.get(id=self.kwargs["product_id"])
    
    def get_id_operation(self):
        id = Operation.objects.count()
        if id == 0:
            return 1
        return id + 1
    
    def get_initial(self):
        product = self.get_product()
        initial = super().get_initial()
        initial['operation']=self.get_id_operation()
        initial['customer']=self.request.user.customer.id
        initial['product']=product
        initial['quantity']=1
        initial['price']=product.price
        return initial

    def validate_available_stock(self, product, quantity):
        if product.retrieve_stock >= quantity:
            return True
        return False

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(**kwargs)                
        context.update({
            'product':self.get_product,
        })        
        return context
    
    def form_valid(self, form):
    
        if form.is_valid():        
                    
            cleaned_data = form.cleaned_data
                        
            type = cleaned_data["operation_type"].name.lower()

            if cleaned_data["customer"].get_account_statement <= 0 and type == 'purchase':
                form.add_error('quantity', 'You do not have sufficient credit for this purchase')
                return self.form_invalid(form)
            
            if cleaned_data["customer"].get_account_statement < cleaned_data["price"] and type == 'purchase':
                form.add_error('quantity', 'You do not have sufficient credit for this purchase')
                return self.form_invalid(form)
                        
            if self.validate_available_stock(cleaned_data["product"], cleaned_data["quantity"]):            
                form.save()
                return super().form_valid(form)
            else:
                form.add_error('quantity', 'Quantity exceded')            
                        
        
        return self.form_invalid(form)
        
    
    
