from django import forms
from .models import AvailableStock, SoldItem

class StockForm(forms.ModelForm):
    class Meta:
        model = AvailableStock
        fields = ['quantity', 'other_fields']  # Include other fields as needed

class SaleForm(forms.ModelForm):
    class Meta:
        model = SoldItem
        fields = ['quantity_sold', 'other_fields']  # Include other fields as needed
