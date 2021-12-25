
from django.db.models import fields
from django.forms import forms, ModelForm, CharField, TextInput, Textarea, BooleanField, CheckboxInput, IntegerField
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

class ProductEditForm(forms.Form):
    title = CharField(max_length=100, widget=TextInput(attrs={'class': 'form-control'}))
    sku = CharField(max_length = 100, widget=TextInput(attrs={'class': 'form-control'}))
    description = CharField(widget=Textarea(attrs={'class': 'form-control'}))
    variant_one_price = IntegerField()
    variant_two_price = IntegerField()
    variant_three_price = IntegerField()
    variant_one_stock = IntegerField()
    variant_two_stock = IntegerField()
    variant_three_stock = IntegerField()

    def save(self):
        cleaned_data = self.cleaned_data
        # product = super(ProductEditForm, self).save(commit=False)
        # product.save()
        # return product
        

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