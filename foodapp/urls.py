from django.urls import path
from . import views

app_name = 'food'

urlpatterns = [
    path('', views.home, name='home'),
    path('food/', views.foodlist, name='food_list'),
    path('food/<slug:slug>/', views.food_detail, name='food_detail'),
    path('food/<slug:slug>/new', views.food_new, name='food_new'),
    path('food/<slug:slug>/edit', views.food_edit, name='food_edit'),
    path('food/<slug:slug>/update', views.food_update, name='food_update'),
]