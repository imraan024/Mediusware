from django.db import models


# Create your models here.
class Variant(models.Model):
    title = models.CharField(max_length=40)
    color = models.CharField(max_length=20, default=None)
    size = models.CharField(max_length=10, default=None)
    description = models.TextField()
    active = models.BooleanField(default=True)
    def __str__(self) -> str:
        return self.title


class Product(models.Model):
    title = models.CharField(max_length=255)
    sku = models.SlugField(max_length=255)
    description = models.TextField()

    def __str__(self) -> str:
        return self.title



class ProductImage(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    file_path = models.URLField()


class ProductVariant(models.Model):
    variant_title = models.CharField(max_length=255)
    variant = models.ForeignKey(Variant, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.variant_title

class ProductVariantPrice(models.Model):
    product_variant_one = models.ForeignKey(ProductVariant, on_delete=models.CASCADE,
                                            related_name='product_variant_one')
    product_variant_two = models.ForeignKey(ProductVariant, on_delete=models.CASCADE,
                                            related_name='product_variant_two')
    product_variant_three = models.ForeignKey(ProductVariant, on_delete=models.CASCADE,
                                              related_name='product_variant_three')
    variant_one_price = models.FloatField(default=0)
    variant_two_price = models.FloatField(default=0)
    variant_three_price = models.FloatField(default=0)
    variant_one_stock = models.FloatField(default=0)
    variant_two_stock = models.FloatField(default=0)
    variant_three_stock = models.FloatField(default=0)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
