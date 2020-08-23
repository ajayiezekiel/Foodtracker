from django import forms

from .models import Food, UnitOfMeasure

class FoodForm(forms.ModelForm):

    class Meta:
        model = Food
        fields = ('food_label', 'unit_of_measure', 'quantity', 'unit_price', 'critical_level',)

    
class FoodEditForm(forms.ModelForm):
    class Meta:
        model = Food
        fields = ('critical_level',)

class FoodUpdateForm(forms.ModelForm):

    class Meta:
        model = Food
        fields = ('label_of_change', 'quantity', 'unit_price')

class CategoryForm(forms.ModelForm):
    class Meta:
        model = UnitOfMeasure
        fields = ('measurement',)
