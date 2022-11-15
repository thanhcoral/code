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
    path('order_detail2/<int:id>', order_detail2, name='order_detail2'),
    path('order_delete/<int:id>', order_delete, name='order_delete'),
    path('order_add', order_add, name='order_add'),
    path('order_add/<int:id>', order_add, name='order_add'),

    path('order_line_add/<int:id>', order_line_add, name='order_line_add'),
    path('order_line_delete/<int:id>', order_line_delete, name='order_line_delete'),

    path('mrp', mrp, name='mrp'),
    path('mrp_list', mrp_list, name='mrp_list'),
    path('mrp_detail/<int:id>', mrp_detail, name='mrp_detail'),
    path('mrp_add', mrp_add, name='mrp_add'),
    path('mrp_add/<int:id>', mrp_add, name='mrp_add'),
    path('mrp_open/<int:id>', mrp_open, name='mrp_open'),
    path('mrp_close/<int:id>', mrp_close, name='mrp_close'),
    path('mrp_process/<int:id>', mrp_process, name='mrp_process'),
    
    path('task_add', task_add, name='task_add'),    
    path('task_add/<int:id>', task_add, name='task_add'),
    path('task_delete/<int:id>', task_delete, name='task_delete'),
    path('task_detail/<int:id>', task_detail, name='task_detail'),
    path('task_start/<int:id>', task_start, name='task_start'),

    path('mf', mf, name='mf'),
    path('mf_detail/<int:id>', mf_detail, name='mf_detail'),

]
