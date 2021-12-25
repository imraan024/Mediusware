from django.views import generic, View
from product.models import ProductVariant, ProductVariantPrice, Variant, Product
from django.views.generic import ListView
from django.views.generic.edit import UpdateView
from product.forms import ProductForm, VariantForm, ProductVariantPriceForm
from django.core.paginator import Paginator
from django.shortcuts import render
from django.urls import reverse_lazy
from django.db.models import Q
import datetime
from django.http import HttpResponseRedirect

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
    paginate_by = 3
    queryset = Product.objects.all()
    context_object_name = 'products'

    def get_context_data(self, **kwargs):
        context = super(ProductListView, self).get_context_data(**kwargs)
        context['product_variants'] = ProductVariantPrice.objects.all()
        context['variants'] = Variant.objects.all()
        return context



class ProductSearchView(ListView):
    template_name = 'products/filter.html'
    paginate_by = 2

    def get_queryset(self):
        title = self.request.GET.get('title')
        variant = self.request.GET.get('variant')
        range_from = self.request.GET.get('price_from')
        range_to = self.request.GET.get('price_to')

        date = self.request.GET.get('date')
        
        



        search_results = Product.objects.filter(
            Q(title__icontains=title)
        )
        if date:
            date = datetime.datetime.strptime(date, '%Y-%m-%d').date()
            search_date = Product.objects.filter(created_at__lte=date)
            search_results = search_results | search_date


        if variant != None:
            variant_search_query = Product.objects.filter(
                (
                    Q(productvariant__variant__color=variant) |
                    Q(productvariant__variant__size=variant)
                )
            )
            search_results = search_results & variant_search_query
        if not range_from and not range_to:
            range_from=0
            range_to=100000
        search_obj = ProductVariantPrice.objects.filter(product__in=search_results)

        pricing_search_results = ProductVariantPrice.objects.filter(
            Q(variant_one_price__range=[range_from, range_to]) |
            Q(variant_two_price__range=[range_from, range_to]) |
            Q(variant_three_price__range=[range_from, range_to])
        )
        new_search_results = search_obj & pricing_search_results

        
            


        return new_search_results

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        product_var = Variant.objects.all()
        product_var_price = ProductVariantPrice.objects.all()
        context['variants'] = product_var
        context['product_variant_price'] = product_var_price
        return context

class EditProductView(UpdateView):
    pk_url_kwarg = 'id'
    template_name = 'products/edit.html'
    model = ProductVariantPrice
    second_model = Product
    form_class = ProductVariantPriceForm
    second_form_class = ProductForm
    success_url = reverse_lazy('product:list.product')

    def get_context_data(self, **kwargs):
        context = super(EditProductView, self).get_context_data(**kwargs)
        context['product'] = True
        if 'form' not in context:
            context['form'] = self.form_class(self.request.GET)
        if 'form2' not in context:
            context['form2'] = self.second_form_class(self.request.GET)
        context['product'] = True
        return context




    