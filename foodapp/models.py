from django.conf import settings
from django.db import models
from django.urls import reverse
from django.utils.translation import gettext_lazy as _


class Category(models.Model):
    name = models.CharField(max_length=200, unique=True, db_index=True)
    slug = models.SlugField(max_length=200, db_index=True, null=True)

    class Meta:
        ordering = ('name',)
        verbose_name = _('category')
        verbose_name_plural = _('categories')
    
    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('product:product_list_by_category', args= [self.slug])

        

class Product(models.Model):
    label_choice = (
        ('P', _('Purchase')),
        ('C', _('Consumed'))
    )
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,related_name='product_created')
    category = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE)
    name = models.CharField(max_length=50, unique=True, db_index=True)
    slug = models.SlugField(max_length=200, db_index=True, null=True)
    unit_of_measure = models.CharField(max_length=50)
    label_of_change = models.CharField(max_length=50, choices=label_choice)
    unit_price = models.DecimalField(default=0, decimal_places=2, max_digits=10)
    quantity = models.PositiveIntegerField(default=0)
    critical_level = models.PositiveIntegerField(default=0)
    is_critical = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = _('product')
        verbose_name_plural = _('products')
        ordering = ('-is_critical',)

    def __str__(self):
        return '{} of {}'.format(self.unit_of_measure, self.name)

    def get_absolute_url(self):
         return reverse('product:product_detail', args=[self.slug])

class Inventory(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,related_name='inventory_created')
    product_item = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='inventory')
    purchased_item = models.PositiveIntegerField(default=0)
    consumed_item = models.PositiveIntegerField(default=0)
    price_per_unit = models.DecimalField(default=0, max_digits=10, decimal_places=2)
    total_cost = models.DecimalField(default=0, max_digits=10, decimal_places=2)
    updated_on = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = _('Inventory')
        verbose_name_plural = _('inventories')
        ordering = ('updated_on',)

    def __str__(self):
        return 'Inventory of {}'.format(self.product_item.name)
