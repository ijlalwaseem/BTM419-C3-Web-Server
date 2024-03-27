#home/forms.py
from django import forms
from .models import Sale, Inventory, Inspection

class SaleForm(forms.ModelForm):
    class Meta:
        model = Sale
        fields = ['product', 'price', 'customer_id']
        labels = {'product': 'Product', 'price': 'Price', 'customer_id': 'Customer ID'}

class InventoryForm(forms.ModelForm):
    class Meta:
        model = Inventory
        fields = ['product', 'quantity']
        labels = {'product': 'Product', 'quantity': 'Quantity'}

class InspectionForm(forms.ModelForm):
    class Meta:
        model = Inspection
        fields = ['vin', 'comments']
        labels = {'vin': 'VIN', 'comments': 'Comments'}