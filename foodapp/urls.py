from django.urls import path
from . import views

app_name = 'food'

urlpatterns = [
    path('', views.foodlist, name='food_list'),
    path('<slug:slug/', views.food_detail, name='food_detail'),
]