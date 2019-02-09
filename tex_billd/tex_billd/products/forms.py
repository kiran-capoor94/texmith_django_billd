from django import forms

from .models import Product


class ProductAddForm(forms.ModelForm):

    class Meta:
        model = Product
        fields = ("name", "company_name", "serial_number", "price",
                  "description", "available_stock", "stock_changed")
