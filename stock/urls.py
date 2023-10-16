from django.urls import path
from . import views

urlpatterns = [
    path('register_stock/', views.register_stock, name='register_stock'),
    path('view_stock/', views.view_stock, name='view_stock'),
    path('register_sold_item/', views.register_sold_item, name='register_sold_item'),
    path('view_sold_items/', views.view_sold_items, name='view_sold_items'),
    path('view_available_stock/', views.view_available_stock, name='view_available_stock'),
]
