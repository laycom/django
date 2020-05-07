from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=64, blank=True, null=True, default=None)
    description = models.TextField(blank=True, null=True, default=None)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)
    price = models.DecimalField(max_digits=10, decimal_places=0, default=0)

    def __str__(self):
        return "Product %s" % (self.name)

    class Meta:
        pass

class ProductImage(models.Model):
    image = models.ImageField(upload_to='static\media\products_images')
    product = models.ForeignKey(Product, on_delete=models.DO_NOTHING, blank=True, null=True, default=None)
    is_active = models.BooleanField(default=True)
    description = models.TextField(blank=True, null=True, default=None)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)