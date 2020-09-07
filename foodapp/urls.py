from django.urls import path
from . import views

app_name = 'product'

urlpatterns = [
    path('', views.home, name='home'),
    path('product/', views.productlist, name='product_list'),
    path('product/new/', views.product_new, name='product_new'),
    path('product/new/<slug:category_slug>/', views.product_new, name='product_new_by_category'),
    path('product/stock/<slug:category_slug>/', views.productlist, name='product_list_by_category'),
    path('product/category/new/', views.category_new, name='category_new'),
    path('product/<slug:slug>/', views.product_detail, name='product_detail'),
    path('product/<slug:slug>/edit/', views.product_edit, name='product_edit'),
    path('product/<slug:slug>/update/', views.product_update, name='product_update'),   
]