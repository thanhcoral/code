from django.contrib import admin
from django.urls import path

from core.views import *

urlpatterns = [
    path('admin/', admin.site.urls),

    path('dashboard', dashboard, name='dashboard'),

    path('customer', customer, name='customer'),
    path('customer_list', customer_list, name='customer_list'),
    path('customer_detail/<int:id>', customer_detail, name='customer_detail'),
    path('customer_delete/<int:id>', customer_delete, name='customer_delete'),
    path('customer_add', customer_add, name='customer_add'),
    path('customer_normal_list', customer_normal_list, name='customer_normal_list'),
    path('customer_potential_list', customer_potential_list, name='customer_potential_list'),


    path('customer_contact_add', customer_contact_add, name='customer_contact_add'),

    path('product', product, name='product'),
    path('product_add', product_add, name='product_add'),
    path('product_list', product_list, name='product_list'),
    path('product_detail/<int:id>', product_detail, name='product_detail'),

    path('sales', order, name='sales'),
    path('order_list', order_list, name='order_list'),
    path('order_detail/<int:id>', order_detail, name='order_detail'),
    path('order_delete/<int:id>', order_delete, name='order_delete'),
    path('order_add', order_add, name='order_add'),
    path('order_add/<int:id>', order_add, name='order_add'),

]
