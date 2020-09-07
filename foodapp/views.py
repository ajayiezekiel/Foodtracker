from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.template.defaultfilters import slugify


from .models import Inventory, Category, Product 
from .forms import ProductForm,ProductCategoryForm ,CategoryForm, ProductEditForm, ProductUpdateForm

# List of foods available to the current user
def home(request):
    return render(request, 'pages/home.html')

@login_required
def productlist(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    products = Product.objects.filter(is_active=True, user=request.user)
    
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)
        
    return render(request, 'pages/list.html', {'category': category,
                                                'categories': categories,
                                                'products': products
                                                })

# Get a particular food item through the unique slug
@login_required
def product_detail(request, slug):
    product = get_object_or_404(Product, slug=slug, is_active=True)

    return render(request, 'pages/detail.html', {'product': product})

# This is for updating Unit of Measure Field
@login_required()
def category_new(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            category = form.save(commit=False)
            category.slug = slugify(category.name)
            category.save()
            return redirect('product:product_list')
    else:
        form = CategoryForm()

    return render(request, 'pages/category_new.html', {'category_form': form})

# Add new food to the database
# @login_required
# def product_new(request):
#     if request.method == 'POST':
#         form = ProductForm(request.POST)
#         if form.is_valid():
#             product = form.save(commit=False)
#             product.slug = slugify(product.name)
#             product.user = request.user
#             # It is assumed that the first food item created in the database should be a purchased food item
#             product.label_of_change = "Purchase"
#             if product.quantity <= product.critical_level:
#                 product.is_critical = True
#             else:
#                 product.is_critical = False
#             product.save()
#             Inventory.objects.create(user=request.user, 
#                                     purchased_item = product.quantity,
#                                     product_item = product,
#                                     price_per_unit = product.unit_price,
#                                     total_cost = product.unit_price * product.quantity
#                                     )
#             return redirect('product:product_detail', slug=product.slug)
#     else:
#         form = ProductForm()
    
#     return render(request, 'pages/product_new.html', {'product_form': form})


# Add new product to the database based on the category
@login_required
def product_new(request, category_slug = None):
    category = None
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        if request.method == 'POST':
            form = ProductCategoryForm(request.POST)
            if form.is_valid():
                product = form.save(commit=False)
                product.slug = slugify(product.name)
                product.user = request.user
                product.category = category
                # It is assumed that the first food item created in the database should be a purchased food item
                product.label_of_change = "Purchase"
                if product.quantity <= product.critical_level:
                    product.is_critical = True
                else:
                    product.is_critical = False
                product.save()
                Inventory.objects.create(user=request.user, 
                                        purchased_item = product.quantity,
                                        product_item = product,
                                        price_per_unit = product.unit_price,
                                        total_cost = product.unit_price * product.quantity
                                        )
                return redirect('product:product_list')
        else:
            form = ProductCategoryForm()
    else:
        if request.method == 'POST':
            form = ProductForm(request.POST)
            if form.is_valid():
                product = form.save(commit=False)
                product.slug = slugify(product.name)
                product.user = request.user
                # It is assumed that the first food item created in the database should be a purchased food item
                product.label_of_change = "Purchase"
                if product.quantity <= product.critical_level:
                    product.is_critical = True
                else:
                    product.is_critical = False
                product.save()
                Inventory.objects.create(user=request.user, 
                                        purchased_item = product.quantity,
                                        product_item = product,
                                        price_per_unit = product.unit_price,
                                        total_cost = product.unit_price * product.quantity
                                        )
                return redirect('product:product_list')
        else:
            form = ProductForm()
    
    return render(request, 'pages/product_new.html', {'product_form': form})



# Edit one of the already saved food item
@login_required
def product_edit(request, slug):
    product = get_object_or_404(Product, slug=slug, is_active=True)
    if request.method == 'POST':
        form = ProductEditForm(request.POST, instance=product)
        if form.is_valid():
            product = form.save(commit=False)
            if product.quantity <= product.critical_level:
                product.is_critical = True
            else:
                product.is_critical = False
            product.save()
            return redirect('product:product_detail', slug=product.slug)
    else:
        form = ProductEditForm(request.POST)
    
    return render(request, 'pages/product_edit.html', {'product_form': form})

@login_required
def product_update(request, slug):
    product = get_object_or_404(Product, slug=slug, is_active=True)
    # This helps to get the current food quantity
    prod_quant = product.quantity
    inventory = get_object_or_404(Inventory, user=request.user, product_item=product)
    if request.method == 'POST':
        form = ProductUpdateForm(request.POST, instance=product)
        if form.is_valid():
            product = form.save(commit=False)
    
            if product.label_of_change == 'Purchase':
                inventory.purchased_item = product.quantity
                product.quantity = prod_quant + product.quantity
            else:
                inventory.consumed_item = product.quantity
                product.quantity = prod_quant - product.quantity

            inventory.total_cost = product.quantity * product.unit_price
            inventory.price_per_unit = product.unit_price
            product.save()
            inventory.save()
            return redirect('product:product_detail', slug=product.slug)
    else:
        form = ProductUpdateForm(request.POST)
    
    return render(request, 'pages/product_update.html', {'product_form': form})







