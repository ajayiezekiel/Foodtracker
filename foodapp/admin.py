from django.contrib import admin

from .models import Food, UnitOfMeasure, Inventory


admin.site.register(UnitOfMeasure)


@admin.register(Food)
class FoodAdmin(admin.ModelAdmin):
    list_display = ['food_label', 'slug', 'unit_of_measure', 'unit_price', 'quantity', 'critical_level', 'created_on', 'updated_on']
    list_filter = ['is_critical', 'created_on', 'updated_on']
    list_editable = ['unit_price', ]
    prepopulated_fields = {'slug': ('food_label',)}

@admin.register(Inventory)
class InventoryAdmin(admin.ModelAdmin):
    list_display = ['food_item', 'purchased_item', 'consumed_item', 'price_per_unit', 'total_cost',]
    list_filter = ['updated_on']
    list_editable = ['price_per_unit',]

# Register your models here.
