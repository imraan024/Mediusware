from django.views import generic, View
from product.models import ProductVariant, ProductVariantPrice, Variant, Product
from django.views.generic import ListView
from django.core.paginator import Paginator
from django.shortcuts import render
from django.urls import reverse_lazy
from django.db.models import Q

class CreateProductView(generic.TemplateView):
    template_name = 'products/create.html'

    def get_context_data(self, **kwargs):
        context = super(CreateProductView, self).get_context_data(**kwargs)
        variants = Variant.objects.filter(active=True).values('id', 'title')
        context['product'] = True
        context['variants'] = list(variants.all())
        return context

class ProductListView(ListView):
    model = Product
    template_name = 'products/list.html'
    paginate_by = 1
    queryset = Product.objects.all()
    context_object_name = 'products'

    def get_context_data(self, **kwargs):
        context = super(ProductListView, self).get_context_data(**kwargs)
        context['product_variants'] = ProductVariantPrice.objects.all()
        context['variants'] = Variant.objects.all()
        return context


    # def get_paginate_by(self, queryset):
    #     if 'product' in queryset:
    #         return super().get_paginate_by(queryset['product'])
    #     else:
    #         return None


# class ProductListView(ListView):
#     model = Product
#     template_name = 'products/list.html'
#     paginate_by = 3


class ProductSearchView(ListView):
    template_name = 'products/filter.html'
    model = Product
    #success_url = reverse_lazy('list.product')

    def get_queryset(self):
        title = self.request.GET.get('title')
        variant = self.request.GET.get('variant')
        object_list = Product.objects.filter(
            Q(title__icontains=title) 
        )
        return object_list
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        product = Product.objects.all()
        product_var = Variant.objects.all()
        product_var_price = ProductVariantPrice.objects.all()
        context['product'] = product
        context['variants'] = product_var
        context['product_variant_price'] = product_var_price
        return context