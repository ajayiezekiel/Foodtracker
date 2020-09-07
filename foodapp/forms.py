from django import forms

from .models import Product, Category

class ProductForm(forms.ModelForm):

    class Meta:
        model = Product
        fields = ('name', 'category', 'unit_of_measure', 'quantity', 'unit_price', 'critical_level',)

class ProductCategoryForm(forms.ModelForm):

    class Meta:
        model = Product
        fields = ('name', 'unit_of_measure', 'quantity', 'unit_price', 'critical_level',)


    
class ProductEditForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ('critical_level',)

class ProductUpdateForm(forms.ModelForm):

    class Meta:
        model = Product
        fields = ('label_of_change', 'quantity', 'unit_price', 'critical_level')

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ('name',)
