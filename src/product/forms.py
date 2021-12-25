from django.db.models.fields import IntegerField
from django.forms import forms, ModelForm, CharField, TextInput, Textarea, BooleanField, CheckboxInput
from django.forms.widgets import NumberInput

from product.models import ProductVariantPrice, Variant, Product


class VariantForm(ModelForm):
    class Meta:
        model = Variant
        fields = '__all__'
        widgets = {
            'title': TextInput(attrs={'class': 'form-control'}),
            'description': Textarea(attrs={'class': 'form-control'}),
            'active': CheckboxInput(attrs={'class': 'form-check-input', 'id': 'active'})
        }

class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = '__all__'
        widgets = {
            'title': TextInput(attrs={'class': 'form-control'}),
            'sku': TextInput(attrs={'class': 'form-control'}),
            'description': Textarea(attrs={'class': 'form-control'}),
        }
class ProductVariantPriceForm(ModelForm):
    class Meta:
        model = ProductVariantPrice
        fields = '__all__'
        widgets = {
            'variant_one_price': NumberInput(attrs={'class': 'form-control'}),
            'variant_two_price': NumberInput(attrs={'class': 'form-control'}),
            'variant_three_price': NumberInput(attrs={'class': 'form-control'}),
            'variant_one_stock': NumberInput(attrs={'class': 'form-control'}),
            'variant_two_stock': NumberInput(attrs={'class': 'form-control'}),
            'variant_three_stock': NumberInput(attrs={'class': 'form-control'}),
        }