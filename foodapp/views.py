from django.shortcuts import render, get_object_or_404, redirect

from .models import Food
from .forms import FoodForm, CategoryForm

# List of foods available to the current user
def foodlist(request):
    food_list = Food.objects.filter(user=request.user)

    return render(request, 'pages/list.html', {'food_list': food_list})

# Get a particular food label through the unique slug
def food_detail(request, slug):
    item = get_object_or_404(Food, slug=slug)

    return render(request, 'pages/detail.html', {'item': item})

# This is for updating Unit of Measure Field
def category_new(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            category = form.save(commit=False)
            category.user = request.user
            category.save()
            return redirect('food_new')
    else:
        form = FoodForm()

    return render()

# Add new food to the database
def food_new(request):
    if request.method == 'POST':
        form = FoodForm(request.POST)
        if form.is_valid():
            food = form.save(commit=False)
            food.user = request.user
            food.label_of_change = "Purchase"
            if food.quantity <= food.critical_level:
                food.is_critical = True
            else:
                food.is_critical = False
            food.save()
            return redirect('food_detail', slug=food.slug)
    else:
        form = FoodForm()
    
    return render(request, 'pages/food_new.html', {'form': food_form})

# Edit one of the already saved food item
def food_edit(request, slug):
    the_food = get_object_or_404(Food, slug=slug)
    if request.method == 'POST':
        form = FoodForm(request.POST, instance=food)
        if form.is_valid():
            food = form.save(commit=False)
            food.user = request.user
            if food.label_of_change == "Purchase":
                food.quantity += the_food.quantity
            else:
                food.quantity = the_food.quantity - food.quantity
            food.save()
            return redirect('food_detail', slug=food.slug)
    else:
        form = FoodForm(request.POST)
    
    return render(request, 'pages/food_edit.html', {'form': food_form})







