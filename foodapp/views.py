from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required


from .models import Food, Inventory
from .forms import FoodForm, CategoryForm, FoodEditForm, FoodUpdateForm

# List of foods available to the current user
def home(request):
    return render(request, 'pages/home.html')

@login_required
def foodlist(request):
    food_list = Food.objects.filter(user=request.user)

    return render(request, 'pages/list.html', {'food_list': food_list})

# Get a particular food label through the unique slug
@login_required
def food_detail(request, slug):
    item = get_object_or_404(Food, slug=slug)

    return render(request, 'pages/detail.html', {'item': item})

# This is for updating Unit of Measure Field
def category_new(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            category = form.save(commit=False)
            category.save()
            return redirect('food_new')
    else:
        form = FoodForm()

    return render()

# Add new food to the database
@login_required
def food_new(request):
    if request.method == 'POST':
        form = FoodForm(request.POST)
        if form.is_valid():
            food = form.save(commit=False)
            food.user = request.user
            # It is assumed that the first food item created in the database should be a purchased food item
            food.label_of_change = "Purchase"
            if food.quantity <= food.critical_level:
                food.is_critical = True
            else:
                food.is_critical = False
            food.save()
            Inventory.objects.create(user=request.user, 
                            purchased_item = food.quantity,
                            food_item = food
                            )
            return redirect('food_detail', slug=food.slug)
    else:
        form = FoodForm()
    
    return render(request, 'pages/food_new.html', {'food_form': form})

# Edit one of the already saved food item
@login_required
def food_edit(request, slug):
    food = get_object_or_404(Food, slug=slug)
    if request.method == 'POST':
        form = FoodEditForm(request.POST, instance=food)
        if form.is_valid():
            food = form.save(commit=False)
            if food.quantity <= food.critical_level:
                food.is_critical = True
            else:
                food.is_critical = False
            food.save()
            return redirect('food_detail', slug=food.slug)
    else:
        form = FoodEditForm(request.POST)
    
    return render(request, 'pages/food_edit.html', {'food_form': form})

@login_required
def food_update(request, slug):
    food = get_object_or_404(Food, slug=slug)
    # This helps to get the current food quantity
    food_quant = food.quantity
    inventory = get_object_or_404(Inventory, user= request.user, label=food)
    if request.method == 'POST':
        form = FoodUpdateForm(request.POST, instance=food)
        if form.is_valid():
            food = form.save(commit=False)
    
            if food.label_of_change == 'Purchase':
                inventory.purchased_item = food.quantity
                food.quantity = food_quant + food.quantity
            else:
                inventory.consumed_item = food.quantity
                food.quantity = food_quant - food.quantity

            inventory.total_cost = food.quantity * food.price
            inventory.price_per_unit = food.price
            food.save()
            inventory.save()
            return redirect('food_detail', slug=food.slug)
    else:
        form = FoodUpdateForm(request.POST)
    
    return render(request, 'pages/food_update.html', {'food_form': form})







