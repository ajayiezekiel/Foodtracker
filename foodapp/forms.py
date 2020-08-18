from django import forms

from .models import Food, UnitOfMeasure

class FoodForm(forms.ModelForm):

    class Meta:
        model = Food
        fields = ('food_label', 'unit_of_measure', 'label_of_change', 'quantity', 'critical_level',)

class CategoryForm(forms.ModelForm):

    class Meta:
        model = UnitOfMeasure
        fields = ('measurement',)
