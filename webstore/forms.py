from django import forms

from catalogs.models import OperationType
from balances.models import Operation

class ShoppingCartForm(forms.ModelForm):
    class Meta:
        model = Operation
        fields = ['operation','customer', 'product', 'quantity', 'price', 'operation_type']
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        self.fields['operation'].widget = forms.HiddenInput()
        self.fields['customer'].widget = forms.HiddenInput()
        self.fields['product'].widget = forms.HiddenInput()