from django import forms
from .models import Product


class ProductForms(forms.ModelForm):
    class Meta:
        model = Product
        fields = [
            'name',
            'details',
            'price',
            'availability',
            'stocks',
            'category',
            'image1',
                    ]

