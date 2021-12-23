from django.views import generic, View
from product.models import ProductVariant, ProductVariantPrice, Variant, Product
from django.views.generic import ListView
from django.core.paginator import Paginator


class CreateProductView(generic.TemplateView):
    template_name = 'products/create.html'

    def get_context_data(self, **kwargs):
        context = super(CreateProductView, self).get_context_data(**kwargs)
        variants = Variant.objects.filter(active=True).values('id', 'title')
        context['product'] = True
        context['variants'] = list(variants.all())
        return context

class ProductListView(generic.TemplateView):
    template_name = 'products/list.html'
    model = Product

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        product = Product.objects.all()
        product_var = Variant.objects.all()
        product_var_price = ProductVariantPrice.objects.all()
        context['product'] = product
        context['variants'] = product_var
        context['product_variant_price'] = product_var_price
        return context