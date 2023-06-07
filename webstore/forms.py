from django import forms

from catalogs.models import OperationType
from balances.models import Operation

class OperationForm(forms.Form):
    customer = forms.CharField(label='Customer', widget=forms.HiddenInput())
    product = forms.CharField(label='Product', widget=forms.HiddenInput())
    quantity = forms.IntegerField(label='Quantity')
    price = forms.DecimalField(label='Price')        
    operation_type = forms.ModelChoiceField(label='Category', queryset=OperationType.objects.all(), required=True)
    
    