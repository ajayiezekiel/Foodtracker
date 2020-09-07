from django.contrib import admin

from .models import Product, Category, Inventory


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}



@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'category', 'slug', 'unit_of_measure', 'unit_price', 'quantity', 'critical_level', 'created_on', 'updated_on']
    list_filter = ['is_critical', 'created_on', 'updated_on']
    list_editable = ['unit_price', ]
    prepopulated_fields = {'slug': ('name',)}

@admin.register(Inventory)
class InventoryAdmin(admin.ModelAdmin):
    list_display = ['product_item', 'purchased_item', 'consumed_item', 'price_per_unit', 'total_cost',]
    list_filter = ['updated_on']
    list_editable = ['price_per_unit',]

# Register your models here.
